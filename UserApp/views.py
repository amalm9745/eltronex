from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from SellerApp.models import ProductModel,ProductImgModel,ProductVariantModel
from AdminApp.models import CategoryModel
from UserApp.models import UserModel,CartModel,UserAddressModel,WishListModel
from django.http import JsonResponse

def HomeFun(request):
    # Fetch category (change "Mobiles" to the desired category name)
    category = CategoryModel.objects.get(category_name="Mobiles")
    # Fetch products for the category
    mobiles = ProductVariantModel.objects.filter(category_id=category)
    
    content = {
        'mobiles': mobiles,
    }

    return render(request, "home.html", content)

def loginFun(request):
    if request.method=="POST":
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        userdata = UserModel.objects.get(user_mobile=mobile)
        if password == userdata.user_password:
            request.session['user'] = userdata.user_id
            print("Session exists:", 'user' in request.session)
            return redirect('/')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})


    return render(request,'login.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect("/")


def product_detail_view(request, product_id,variant_id):
   
    # Retrieve the product details
    product = get_object_or_404(ProductModel, pk=product_id)
    if product.sub_category_id.category_id.category_name=="Mobiles":
        ram=[]
        rom=[]
        color=[]
        var= ProductVariantModel.objects.filter(product_id=product_id)
        for x in var:
            ram.append(x.ram)
            rom.append(x.storage)
            color.append(x.color)

        filter={
            'Ram':ram,
            'Storage':rom,
            'Color':color
        } 
        variant=get_object_or_404(ProductVariantModel,pk=variant_id)
        highlight={
            'Ram':variant.ram,
            'Storage':variant.storage,
            'Display':variant.display,
            'Camera':variant.camera,
            'Battery':variant.battery,
            'Processor':variant.processor
        }
        product_img = ProductImgModel.objects.filter(variant_id=variant_id)

    


    product_in_cart = False
    product_in_wishlist = False
    if 'user' in request.session:
        user = request.session['user']
        product_in_cart = CartModel.objects.filter(user_id=user, variant_id=variant_id).exists()
        product_in_wishlist=WishListModel.objects.filter(user_id=user, variant_id=variant_id).exists()
    
    content={
        'product': variant,
        'product_img':product_img,
        'product_in_cart':product_in_cart,
        'highlight':highlight,
        'filter':filter,
        'product_in_wishlist':product_in_wishlist

    }
    return render(request, 'product_details.html', content)



def addToCart(request,variant_id,location):

    if 'user' in request.session:
        user = request.session['user']
        if location=="product_details":
            cart=CartModel()
            variant_id=ProductVariantModel.objects.get(variant_id=variant_id)
            cart.variant_id=variant_id
            cart.user_id=UserModel.objects.get(user_id=user)
            cart.quantity=1
            cart.save()
            return redirect('/cart')
        elif location=="wishlist":
            
            if CartModel.objects.filter(variant_id=variant_id).exists():
                item=WishListModel.objects.filter(variant_id=variant_id)
                item.delete()
                return redirect('/wishlist')
            else:
                cart=CartModel()
                variant_id=ProductVariantModel.objects.get(variant_id=variant_id)
                cart.variant_id=variant_id
                cart.user_id=UserModel.objects.get(user_id=user)
                cart.quantity=1
                cart.save()
                item=WishListModel.objects.filter(variant_id=variant_id)
                item.delete()
                return redirect('/wishlist')
        else:
            return HttpResponse("Some error occurs")
    else:
        return redirect('/login')


def cartFun(request):
    if 'user' in request.session:
        if request.method == 'POST':
            # Check if the request is for updating quantity
            if 'product_id' in request.POST and 'quantity' in request.POST:
                product_id = request.POST['product_id']
                quantity = request.POST['quantity']
                try:
                    cart_item = CartModel.objects.get(user_id=request.session['user'], variant_id=product_id)
                    cart_item.quantity = quantity
                    cart_item.save()
                    cart_items = CartModel.objects.filter(user_id=request.session['user'])
                    total_cart_value = 0
                    for cart_item in cart_items:
                        value=int(cart_item.variant_id.selling_price) * cart_item.quantity
                        total_cart_value += value
                        print(total_cart_value)
                    return JsonResponse({'success': True, 'total_cart_value': total_cart_value})
                except CartModel.DoesNotExist:
                    return JsonResponse({'success': False, 'error': 'Cart item not found'})
        else:
            cart_items=CartModel.objects.filter(user_id=request.session['user'])
            product_with_total_price = []
            total_cart_value = 0
            product_image=''

            for cart_item in cart_items:
                product_image = ProductImgModel.objects.filter(variant_id=cart_item.variant_id).first()
                # Calculate total price for each book based on quantity
                # total_price = cart_item.quantity * float(cart_item.product_id.selling_price)
                value=int(cart_item.variant_id.selling_price) * cart_item.quantity
                total_cart_value +=value

                # Append product with total price to the list
                product_with_total_price.append({
                    'product': cart_item.variant_id,
                    'quantity': cart_item.quantity,
                    'product_image':product_image
                })
            return render(request, 'cart_page.html', {"product": product_with_total_price, "total_cart_value": total_cart_value})
    else:
        return redirect('/login')
    

def removeCartItem(request,variant_id):
    product=CartModel.objects.filter(variant_id=variant_id)
    product.delete()
    return redirect('/cart')


def myProfile(request):
    if 'user' in request.session:
        user=request.session['user']
        current_user=UserModel.objects.get(user_id=user)
        user_address=UserAddressModel.objects.filter(user_id=user)
        editAddressDetail=""
        if request.method=="POST":
            form_id=request.POST.get('profile')
            if form_id=='profile':
                name=request.POST.get('name')
                mobile=request.POST.get('mobile')
                email=request.POST.get('email')
                gender=request.POST.get('gender')
                current_user=UserModel.objects.get(user_id=user)
                current_user.user_name=name
                current_user.user_mobile=mobile
                current_user.user_email=email
                current_user.gender=gender
                current_user.save()
            if form_id=="address":
                name=request.POST.get('name')
                mobile=request.POST.get('mobile')
                address=request.POST.get('address')
                locality=request.POST.get('locality')
                pincode=request.POST.get('pincode')
                city=request.POST.get('city')
                state=request.POST.get('state')
                landmark=request.POST.get('landmark')
                address_type=request.POST.get('addresstype')
                user_id=UserModel.objects.get(user_id=user)
                new_address=UserAddressModel(name=name,mobile=mobile,address=address,locality=locality,
                                             pincode=pincode,city=city,state=state,landmark=landmark,
                                             address_type=address_type,user_id=user_id)
                
                new_address.save()
            if form_id=="editAddressSave":
                address_id=request.POST.get('addressId')
                name=request.POST.get('editName')
                mobile=request.POST.get('editMobile')
                address=request.POST.get('editAddress')
                locality=request.POST.get('editLocality')
                pincode=request.POST.get('editPincode')
                city=request.POST.get('editCity')
                state=request.POST.get('editState')
                landmark=request.POST.get('editLandmark')
                address_type=request.POST.get('editAddresstype')
                edit_address=UserAddressModel.objects.get(address_id=address_id)
                edit_address.name=name
                edit_address.mobile=mobile
                edit_address.address=address
                edit_address.locality=locality
                edit_address.pincode=pincode
                edit_address.city=city
                edit_address.state=state
                edit_address.landmark=landmark
                edit_address.address_type=address_type
                edit_address.save()

        return render(request,"myprofile.html",{"user":current_user,"address":user_address,"editAddressDetail":editAddressDetail})
    
def removeAddress(request,address_id):
    address=UserAddressModel.objects.get(address_id=address_id)
    address.delete()
    return redirect('/myprofile')


def moveToWishlist(request,variant_id):
    user = request.session['user']
    if WishListModel.objects.filter(variant_id=variant_id).exists():
        item=CartModel.objects.filter(variant_id=variant_id)
        item.delete()
        return redirect('/Cart')
    else:
        wishlist=WishListModel()
        variant_id=ProductVariantModel.objects.get(variant_id=variant_id)
        wishlist.variant_id=variant_id
        wishlist.user_id=UserModel.objects.get(user_id=user)
        wishlist.save()
        item=CartModel.objects.filter(variant_id=variant_id)
        item.delete()
        return redirect('/Cart')




def addToWishlist(request, variant_id):
    response_data = {}
    
    if 'user' in request.session:
        user = request.session['user']
        
        # Check if the product is already in the wishlist
        if WishListModel.objects.filter(user_id=user, variant_id=variant_id).exists():
            # Remove the product from the wishlist
            wish_list_item=WishListModel.objects.filter(variant_id=variant_id)
            wish_list_item.delete()
            
            response_data['success'] = True
        else:
            # Add the product to the wishlist

            wish_list_item = WishListModel()
            id=ProductVariantModel.objects.get(variant_id=variant_id)
            wish_list_item .variant_id=id
            wish_list_item .user_id=UserModel.objects.get(user_id=user)
            wish_list_item.save()
            response_data['success'] = True
    else:
        response_data['success'] = False
    
    return JsonResponse(response_data)


def wishlistView(request):
    if 'user' in request.session:
        wishlist_items = WishListModel.objects.filter(user_id=request.session['user'])
        products_details=[]
        for item in wishlist_items:
            product_image=ProductImgModel.objects.filter(variant_id=item.variant_id).first()
            products_details.append({
                    'product': item.variant_id,
                    'product_image':product_image
                })

        
        return render(request, 'wishlist_page.html', {"products": products_details})
    else:
        return redirect('/login')
    
def removeWishlistItem(request,variant_id):
    item=WishListModel.objects.filter(variant_id=variant_id)
    item.delete()
    return redirect('/wishlist')

def checkout(request):
    cart_items = CartModel.objects.filter(user_id=request.session['user'])
    products = []
    for item in cart_items:
       product_image=ProductImgModel.objects.filter(variant_id=item.variant_id).first()
       products.append({
            'product': item.variant_id,
            'product_image':product_image,
            'quantity':item.quantity
        })
    return render(request,'checkout.html',{'products':products})