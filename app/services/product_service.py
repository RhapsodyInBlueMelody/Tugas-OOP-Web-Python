import httpx
import asyncio

class ProductService:
    BASE_URL = 'https://fakestoreapi.com/products'
    
    @classmethod
    def get_products_by_category(cls, category):
        """Get all products in a category"""
        async def fetch_products():
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(f"{cls.BASE_URL}/category/{category}")
                    if response.status_code == 200:
                        return response.json()
                    return []
            except httpx.RequestError:
                return []
        
        # Use asyncio.run to fully resolve the coroutine
        return asyncio.run(fetch_products())
    
    @classmethod
    def create_product(cls, product):
        """Send a POST request to create a new product"""
        try:
            with httpx.Client() as client:
                # Prepare the payload exactly as shown in the documentation
                payload = {
                    'title': product.title,
                    'price': product.price,
                    'description': product.description,
                    'image': product.image,
                    'category': product.category
                }
            
                # Ensure you're sending JSON with correct headers
                response = client.post(
                    cls.BASE_URL, 
                    json=payload,
                    headers={'Content-Type': 'application/json'}
                )
            
                # Log the response for debugging
                print(f"Response Status: {response.status_code}")
                print(f"Response Content: {response.text}")
            
                if response.status_code == 200:  # Note: API returns 200, not 201
                    return response.json()
                else:
                    return f"Error adding product: {response.status_code} - {response.text}"
    
        except httpx.RequestError as e:
            return f"Error connecting to the API: {str(e)}"
    
    @classmethod
    def get_product(cls, product_id):
        """Get a single product by ID"""
        async def fetch_product():
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(f"{cls.BASE_URL}/{product_id}")
                    if response.status_code == 200:
                        return response.json()
                    return None
            except httpx.RequestError:
                return None
        
        # Use asyncio.run to fully resolve the coroutine
        return asyncio.run(fetch_product())
