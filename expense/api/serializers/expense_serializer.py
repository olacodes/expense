from rest_framework import serializers

from ..models.expense import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(read_only=
    # True, many=True)
    class Meta:
        model = Expense
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.value = validated_data.get('value', instance.value)
            instance.reason = validated_data.get('reason', instance.reason)
            # instance.user_id = validated_data.get('user_id', instance.user_id)
            # instance.date_added = validated_data.get('date_added', instance.date_added)
            # instance.last_modified = validated_data.get('last_modified', instance.last_modified)
            
            instance.save()
            return instance

