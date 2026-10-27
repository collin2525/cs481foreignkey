from django.shortcuts import render
from django.views import View
from .models import Owner, Species, Pet


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})

class AddOwner(View):
    def get(self, request):
        owners = list(Owner.objects.all().values())
        return render(request, 'addOwner.html', {"owners": owners})

    def post(self, request):
        name = request.POST.get("name", "")
        owner = Owner(name=name, balance=0)
        owner.save()
        owners = list(Owner.objects.all().values())
        return render(request, 'addOwner.html', {"owners": owners})


class AddPet(View):
    def get(self, request):
        owners = list(Owner.objects.all().values())
        species = list(Species.objects.all().values())
        return render(request, 'addPet.html', {"owners": owners, "species": species, "pets": []})

    def post(self, request):
        print(request.POST)
        name = request.POST.get("name", "")
        ownerid = int(request.POST.get("myOwner", ""))
        speciesid = int(request.POST.get("mySpecies", ""))
        owner = Owner.objects.get(id=ownerid)
        species = Species.objects.get(id=speciesid)
        pet = Pet(name=name, owner=owner, species=species)
        pet.save()
        owners = list(Owner.objects.all().values())
        species = list(Species.objects.all().values())
        rawPets = list(Pet.objects.all().values())
        pets = []
        for i in rawPets:
            newPet = {}
            newPet["name"] = i["name"]
            newPet["owner"] = str(Owner.objects.get(id=i["owner_id"]))
            newPet["species"] = str(Species.objects.get(id=i["species_id"]))
            pets.append(newPet)
        return render(request, 'addPet.html', {"owners": owners, "species": species, "pets": pets})


class OBS(View):
    pass


class PetsByOwner(View):
    def get(self, request):
        return render(request, 'pbo.html', {"owners": list(Owner.objects.all()), "pets": []})

    def post(self, request):
        owner_name = request.POST["owner"]
        pets = list(Pet.objects.filter(owner__name=owner_name))
        owners = list(Owner.objects.all())
        return render(request, 'pbo.html', {"owners": owners, "pets": pets})

