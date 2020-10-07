from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
# from rest_framework import routers, serializers, viewsets, status

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from RestAPI.models import Vendor, Bidder
# from django.views.decorators.csrf import csrf_exempt


# VIEW SETS

class Register(APIView):
    def get(self, request):
        return Response({"success": False, "message": "GET Method not allowed"}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        try:
            # EXTRACTING DATA FROM REQUEST
            data = request.data
            usertype = data['usertype']
            firstname , lastname , email , password = data['firstname'] , data['lastname'] , data['email'] , data['password']
            companyname = data['companyname']
            mobilenumber = data['mobilenumber']
            telephone = data['telephone']
            address1 = data['address1']
            address2 = data['address2']
            city = data['city']
            postalzip = data['postalzip']
            country = data['country']
            state = data['state']
            # PROCESSING DATA
            if(usertype == 'vendor'):
                print('creating vendor')
                group = Group.objects.get(name='vendor')
                try:
                    user = User.objects.create_user(
                        username=email, 
                        email=email, 
                        password=password, 
                        first_name=firstname, 
                        last_name= lastname
                    )
                except:
                    return Response({"success": False, "message": "User with given email already exists. Please Login."}, status=status.HTTP_200_OK)
                user.groups.add(group)
                user.save()
                Vendor.objects.create(
                    Vendor = user, 
                    CompanyName = companyname, 
                    MobileNumber = mobilenumber,
                    Telephone = telephone,
                    Address1 = address1,
                    Address2 = address2,
                    City = city,
                    PostalZip = postalzip,
                    Country = country,
                    State = state
                )
            elif(usertype == 'bidder'):
                print('creating bidder')
                group = Group.objects.get(name='bidder')
                try:
                    user = User.objects.create_user(
                        username=email, 
                        email=email, 
                        password=password, 
                        first_name=firstname, 
                        last_name= lastname
                    )
                except:
                    return Response({"success": False, "message": "User with given email already exists. Please Login."}, status=status.HTTP_200_OK)
                user.groups.add(group)
                user.save()
                Bidder.objects.create(
                    Bidder = user, 
                    CompanyName = companyname, 
                    MobileNumber = mobilenumber,
                    Telephone = telephone,
                    Address1 = address1,
                    Address2 = address2,
                    City = city,
                    PostalZip = postalzip,
                    Country = country,
                    State = state
                )
            else:
                return Response({"success": False, "message": "Invalid usertype. usertype must be either 'bidder' or 'vendor'."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": True, "message": "User Created"}, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response({"success": False, "message": "JSON type is required."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"success": False, "message": "Invalid Data Sent."}, status=status.HTTP_400_BAD_REQUEST)

#usertype == vendor , bidder
#Register API request expected :

# {
#     "usertype" : "vendor" ,
#     "firstname" : "test" ,
#     "lastname" : "vendortest" ,
#     "email" : "email@email.com" ,
#     "password" : "pass1234" ,
#     "companyname" : "NoComp" ,
#     "mobilenumber" : "123456789" ,
#     "telephone" : "123456789" ,
#     "address1" : "12, ABC Road" ,
#     "address2" : "PQR Street" ,
#     "city" : "Kolkata" ,
#     "postalzip" : "700033" ,
#     "country" : "India" ,
#     "state" : "WB" 
# }
