from django.db import models
from django.contrib.auth.models import User

class Gift(models.Model):
    """
    Gift model represents an item that a user wishes to receive as a gift.

    Attributes:
        gift_id (AutoField): A unique identifier for each gift, automatically generated.
        gift_receiver (ForeignKey): A reference to the User who is intended to receive the gift. 
                                     This sets up a many-to-one relationship with the User model.
        item_name (CharField): The name or description of the gift.
        exact_item (BooleanField): Indicates whether an exact item is being requested, or just a type.
                                   'True' means the exact item is requested, 'False' allows for similar items.
        multiple (BooleanField): Indicates whether multiple instances of this gift are acceptable.
                                 Useful for items where having more than one is desirable.
        notes (CharField): Additional notes or details about the gift, can be left blank.
        date_to_remove (DateField): An optional field indicating when this gift should be removed from the list,
                                    useful for time-sensitive gifts, and for keeping the list clean once an item is marked as bought. Can be null.
        bought (BooleanField): Indicates whether the gift has been purchased.
        visible_to (ManyToManyField): A list of Users who are allowed to view this gift. This field allows
                                      the gift to be visible to specific users, beyond just the gift receiver.
        added_by (ForeignKey): A reference to the User who added the gift, establishing who is responsible
                               for the entry of this gift.

    The 'visible_to' field uses 'related_name' to enable reverse access from User to view all gifts
    visible to a particular user using 'user.visible_gifts.all()'.
    """
    gift_id = models.AutoField(primary_key=True)
    gift_receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    exact_item = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    notes = models.CharField(max_length=1000, blank=True)
    date_to_remove = models.DateField(blank=True, null=True, default=None)
    bought = models.BooleanField(default=False)
    visible_to = models.ManyToManyField(User, related_name='visible_gifts', blank=True) # Make default all
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 

class Link(models.Model):
    """
    Link model represents a URL associated with a Gift.

    Each Link instance is related to a specific Gift and stores a URL.
    This allows for the storage of multiple links or references for a single Gift,
    enabling users to provide various online resources or purchase options related to the gift.

    Attributes:
        gift (ForeignKey): A foreign key that links the Link to its associated Gift.
        url (URLField): The URL to be associated with the Gift.

    The `related_name='urls'` property in the ForeignKey definition allows each Gift to access
    its associated links directly using `gift.urls`.
    """

    gift = models.ForeignKey(Gift, related_name='urls', on_delete=models.CASCADE)
    url = models.URLField(max_length=400)
