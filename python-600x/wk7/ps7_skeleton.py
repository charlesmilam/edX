import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.adoption_center = {}
        self.adoption_center['name'] = name
        self.adoption_center['species_types'] = species_types
        self.adoption_center['location'] = location

    def get_number_of_species(self, animal):
        return self.adoption_center['species_types'][animal]

    def get_location(self):
        return self.adoption_center['location']

    def get_species_count(self):
        return self.adoption_center.copy()

    def get_name(self):
        return self.adoption_center['name']

    def adopt_pet(self, species):
        if species in self.adoption_center['species_types']:
            self.adoption_center['species_types'][species] -= 1
            # remove the key if <= 0
            if self.adoption_center['species_types'] <= 0:
                self.adoption_center['species_types'].pop(species)


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        pass

    def get_name(self):
        pass

    def get_desired_species(self):
        pass

    def get_score(self, adoption_center):
        pass



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    pass # should contain an __init__ and a get_score method.


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    pass # should contain an __init__ and a get_score method.


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    pass # should contain an __init__ and a get_score method.


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    pass # should contain an __init__ and a get_score method.


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    pass # should contain an __init__ and a get_score method.


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    pass

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    pass


# Test - create an instance of an adoption center
ac_name = 'Test One'
ac_species_types = {"Dog": 10, "Cat": 5, "Lizard": 3}
ac_location = (1.0, 3.0)
test_center = AdoptionCenter(ac_name, ac_species_types, ac_location)
print 'Should return an object with correct values:'
print test_center.adoption_center
print
print '-' * 15
print

# Test - get_number_of_species for a given animal
print 'Should return the correct number of animals for a given species'
print 'Expect: 10'
print 'Actual:', test_center.get_number_of_species('Dog')
print
print '-' * 15
print

# Test - get_location for an adoption center
print 'Should return the correct location for an adoption center'
print 'Expect: (1.0, 3.0)'
print 'Actual:', test_center.get_location()
print
print '-' * 15
print

# Test - get_species_count for an adoption center
print 'Shoud return a copy of the adoption center object'
print 'Expect: False'
print 'Actual:', test_center.get_species_count() is test_center.adoption_center
print
print '-' * 15
print

# Test - get_name for an adoption center
print 'Should return the correct name for an adoption center'
print 'Expect: Test One'
print 'Actual:', test_center.get_name()
print
print '-' * 15
print

# Test - adopt_pet from an adoption center
print 'Should correctly decrement the count for a given species'
print 'Expect Dog to be: 9'
test_center.adopt_pet('Dog')
print 'Actual Dog is:', test_center.get_number_of_species('Dog')
