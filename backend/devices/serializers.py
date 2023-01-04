from rest_framework import serializers

from .models import Device, Features


class FeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Features
        fields = ('feature', 'unit', 'value')


class DeviceSerializer(serializers.ModelSerializer):
    features = FeaturesSerializer(many=True,  required=False)

    class Meta:
        model = Device
        fields = ('name', 'ip_adress', 'description', 'features')

    def create(self, validated_data):
        if 'features' not in self.initial_data:
            device = Device.objects.create(**validated_data)
            return device

        features = validated_data.pop('features')
        device = Device.objects.create(**validated_data)
        for feature in features:
            Features.objects.create(device=device, **feature)
        return device

    def update(self, instance, validated_data):
        if 'features' not in self.initial_data:
            instance.name = validated_data.get("name", instance.name)
            instance.ip_adress = validated_data.get("ip_adress",
                                                    instance.ip_adress)
            instance.description = validated_data.get("description",
                                                      instance.description)
            instance.save()
            return instance

        features = validated_data.pop('features')
        instance.name = validated_data.get("name", instance.name)
        instance.ip_adress = validated_data.get("ip_adress",
                                                instance.ip_adress)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.save()
        current_features = instance.features.all()
        for i, feature in enumerate(features):
            dict_feature = dict(feature)
            current_feature = current_features[i]
            current_feature.feature = dict_feature.get("feature",
                                                       current_feature.feature)
            current_feature.unit = dict_feature.get("unit",
                                                    current_feature.unit)
            current_feature.value = dict_feature.get("value",
                                                     current_feature.value)
            current_feature.save()
        return instance
