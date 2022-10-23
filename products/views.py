from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category, ProductReview
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    Function to add product review
    """

    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Product Review Added.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add your review,n\
                            please check the review form ')

        review_form = ReviewForm()
        context = {
            'product': product,
            'review_form': review_form,
        }
    return render(request, 'products/product_detail.html', context)


@login_required
def edit_review(request, review_id):
    """
    Edit exisiting review
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    if request.user != review.user:
        messages.error(request, (
                                'You have no permission to access this page'
                                ))
        return redirect('home')
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.info(request, 'Your review has been updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, (
                                    'Failed to edit the review. Please ensure'
                                    'the form is valid.'))

    else:
        review_form = ReviewForm(instance=review)

    messages.info(request, 'You are updating your review')
    context = {
        'review_form': review_form,
        'review': review,
        'product': product,
    }
    return render(request, 'products/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    View to delete reviews
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    current_user = UserProfile.objects.get(user=request.user)
    if review.user != current_user and not request.user.is_superuser:
        messages.error(request, 'You are trying to delete a review by someone else.')
        return redirect(reverse('product_detail', args=[product.id]))
    if review.user == current_user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Your Review is deleted!')
    return redirect(reverse('product_detail', args=[product.id]))