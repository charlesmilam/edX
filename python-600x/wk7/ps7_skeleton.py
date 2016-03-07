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
        self.adoption_center['location'] = tuple (map (float, location))

    def get_number_of_species(self, animal):
        try:
            return self.adoption_center['species_types'][animal]
        except:
            return 0

    def get_location(self):
        return self.adoption_center['location']

    def get_species_count(self):
        return self.adoption_center['species_types'].copy()

    def get_name(self):
        return self.adoption_center['name']

    def adopt_pet(self, species):
        if species in self.adoption_center['species_types']:
            self.adoption_center['species_types'][species] -= 1
            # remove the key if <= 0
            if self.adoption_center['species_types'][species] <= 0:
                self.adoption_center['species_types'].pop(species)


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        return float(1 * adoption_center.get_number_of_species(self.desired_species))


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        considered_species_count = 0
        for species in self.considered_species:
            considered_species_count += adoption_center.get_number_of_species(species)

        return float(Adopter.get_score(self, adoption_center) + (considered_species_count * .3))

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        score = float(Adopter.get_score(self, adoption_center) - (adoption_center.get_number_of_species(self.feared_species) * .3))

        if score < 0:
            return 0.0
        else:
            return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for species in self.allergic_species:
            if species in adoption_center.get_species_count():
                return 0.0

        return float(Adopter.get_score(self, adoption_center))


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        most_allergic = 1.0
        for species in self.allergic_species:
            if species in adoption_center.get_species_count():
                if self.medicine_effectiveness[species] < most_allergic:
                    most_allergic = self.medicine_effectiveness[species]

        return float(Adopter.get_score(self, adoption_center) * most_allergic)


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
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        return ((self.location[0] - to_location[0])**2 + (self.location[1] - to_location[1])**2)**.5

    def get_score(self, adoption_center):
        lin_dist = self.get_linear_distance(adoption_center.get_location())

        if lin_dist < 1:
            return Adapter.get_score(self.desired_species)
        elif 1 <= lin_dist < 3:
            modifier = rand.uniform(.7, .9)
            return adoption_center.get_number_of_species(self.desired_species) * modifier
        elif 3 <= lin_dist < 5:
            modifier = rand.uniform(.5, .7)
            return adoption_center.get_number_of_species(self.desired_species) * modifier
        elif lin_dist >= 5:
            modifier = rand.uniform(.1, .5)
            return adoption_center.get_number_of_species(self.desired_species) * modifier



def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    ac_list = []
    for ac in list_of_adoption_centers:
        ac_list.append({'ac': ac, 'score': adopter.get_score(ac)})

    print ac_list
    sorted_ac_list = sorted(ac_list, key=lambda k: (k['score'], k['ac'].get_name()), reverse=True)
    final_list = []
    for item in sorted_ac_list:
        final_list.append(item['ac'])
    print sorted_ac_list
    print final_list
    return final_list

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    pass


# Test - create an instance of an adoption center
ac_name = 'Test One'
ac_species_types = {"Dog": 10, "Cat": 5, "Lizard": 3, 'Bird': 7, 'Rabbit': 1}
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

# Test - get_number_of_species for a given animal
print 'Should not error if species not in species_types'
test_center.get_number_of_species('Bird')
print 'There should be no error'
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
print 'Actual:', test_center.get_species_count() is test_center.adoption_center['species_types']
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
print
print '-' * 15
print

# Test - adopt_pet from an adoption center
print 'Should correctly decrement the count for a given species, and remove the key when it reaches 0'
print 'Expect Lizard to be: 2'
test_center.adopt_pet('Lizard')
print 'Actual Lizard is:', test_center.get_number_of_species('Lizard')
print 'Expect Lizard to be: 1'
test_center.adopt_pet('Lizard')
print 'Actual Lizard is:', test_center.get_number_of_species('Lizard')
test_center.adopt_pet('Lizard')
print 'Expect Lizard to not be list of species'
print test_center.get_species_count()
test_center.adopt_pet('Lizard')
print 'Should not generate an error when searching for non-existent key'
print
print '-' * 15
print

# Test - create an adopter
ad_name = 'Chuck'
ad_species = 'Dog'
test_adopter = Adopter(ad_name, ad_species)
print 'Should return an instance of an adopter:'
print test_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Chuck'
print 'Actual:', test_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 9.0'
print 'Actual:', test_adopter.get_score(test_center)
print
print '-' * 15
print

# Test - create a flexible adopter
ad_name = 'Grace'
ad_species = 'Dog'
ad_con_species = ['Cat', 'Bird', 'Rabbit']
test_flex_adopter = FlexibleAdopter(ad_name, ad_species, ad_con_species)
print 'Should return an instance of an adopter:'
print test_flex_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Chuck'
print 'Actual:', test_flex_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_flex_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 12.9'
print 'Actual:', test_flex_adopter.get_score(test_center)
print
print '-' * 15
print

# Test - create a fearful adopter
ad_fear_name = 'Alli'
ad_fear_desirespecies = 'Dog'
ad_fear_species = 'Rabbit'
test_fear_adopter = FearfulAdopter(ad_fear_name, ad_fear_desirespecies, ad_fear_species)
print 'Should return an instance of an adopter:'
print test_fear_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Alli'
print 'Actual:', test_fear_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_fear_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 8.7'
print 'Actual:', test_fear_adopter.get_score(test_center)
print
print '-' * 15
print

# Test - create an allergic adopter
ad_allergic_name = 'Rose'
ad_allergic_desirespecies = 'Dog'
ad_allergic_species = ['Rabbit', 'Lizard']
test_allergic_adopter = AllergicAdopter(ad_allergic_name, ad_allergic_desirespecies, ad_allergic_species)
print 'Should return an instance of an adopter:'
print test_allergic_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Rose'
print 'Actual:', test_allergic_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_allergic_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 0.0'
print 'Actual:', test_allergic_adopter.get_score(test_center)
print
print '-' * 15
print

{"Dog": 0.5, "Cat": 0.0, "Horse": 1.0}
# Test - create an medicated allergic adopter
ad_med_allergic_name = 'Bop'
ad_med_allergic_desirespecies = 'Dog'
ad_med_allergic_species = ['Horse', 'Bird']
ad_medicated_species = {"Bird": 0.5, "Cat": 0.0, "Horse": 1.0}
test_med_allergic_adopter = MedicatedAllergicAdopter(ad_med_allergic_name, ad_med_allergic_desirespecies, ad_med_allergic_species, ad_medicated_species)
print 'Should return an instance of an adopter:'
print test_med_allergic_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Bop'
print 'Actual:', test_med_allergic_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_med_allergic_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 4.5'
print 'Actual:', test_med_allergic_adopter.get_score(test_center)
print
print '-' * 15
print

# Test - create a sluggish adopter
# test cases
# (0, 0) (10.0, 3.0)
# 1.35516525037
# (0, 0) (8.0, -5.0)
# 23.3363694486
# (0, 0) (2.2, -3.3)
# 14.6128279803
# (0, 0) (9.0, 9.0)
# 3.85860990005
# (0, 0) (-9.9, -2.0)
# 0.0
ac1_name = 'Test Two'
ac1_species_types = {"Dog": 10, "Cat": 5, "Lizard": 3, 'Bird': 7, 'Rabbit': 1}
ac1_location = (2.2, -3.3)
test_center2 = AdoptionCenter(ac1_name, ac1_species_types, ac1_location)
ad_slug_name = 'Dottie'
ad_slug_species = 'Dog'
slug_locn = (0, 0)
test_slug_adopter = SluggishAdopter(ad_name, ad_species, slug_locn)
print 'Should return an instance of an adopter:'
print test_slug_adopter
print
print 'Should return the correct adopter name'
print 'Expect: Chuck'
print 'Actual:', test_slug_adopter.get_name()
print
print 'Should return the correct desired species'
print 'Expect: Dog'
print 'Actual:', test_slug_adopter.get_desired_species()
print
print 'Should return the correct score'
print 'Expect: 28.0064139901'
print 'Actual:', test_slug_adopter.get_score(test_center2)
print
print '-' * 15
print

# Test - get_ordered_adoption_center_list and get_adopters_for_advertisement
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog")

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned
