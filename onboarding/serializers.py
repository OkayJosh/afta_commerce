from rest_framework.serializers import ModelSerializer

from onboarding.models import Business, Product


class BusinessSerializers(ModelSerializer):
    class Meta:
        model = Business
        fields = [
            'name', 'user', 'industry',
            'description', 'address', 'contact_number',
            'cac', 'compliance', 'id'
        ]


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'business',
            'description', 'price',
            'quantity', 'id'
        ]
