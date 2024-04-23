from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    """
    The Member model represents a user in the system, a participant in the gift exchange process.

    Attributes:
        member_id (AutoField): A unique identifier for each member, automatically generated.
        member_name (CharField): The name of the member.
        show_bought (BooleanField): A flag to indicate whether this member chooses to see gifts that have already been purchased. 'True' means the member wants to see bought gifts, 'False' means they do not.
    """
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=50)
    show_bought = models.BooleanField(default=True)


class Link(models.Model):
    """
    The Link model represents a single URL associated with a Gift.

    Attributes:
        url (URLField): The URL associated with the Gift.
        name (CharField): The name or description of the URL.
    """
    url = models.URLField(max_length=400)
    name = models.CharField(max_length=100, blank=True)

class Gift(models.Model):
    """
    The Gift model represents an item that a member wishes to receive as a gift.

    Attributes:
        gift_id (AutoField): A unique identifier for each gift, automatically generated.
        gift_adder (ForeignKey): A reference to the Member who added the gift, establishing who is responsible for the entry of this gift. This sets up a many-to-one relationship with the Member model.
        gift_receiver (ForeignKey): A reference to the Member who is intended to receive the gift. This sets up another many-to-one relationship with the Member model.
        item_name (CharField): The name or description of the gift.
        links (ManyToManyField): A list of Links associated with this gift. This field allows for associating multiple URLs with the gift.
        exact_item (BooleanField): Indicates whether an exact item is being requested, or just a type. 'True' means the exact item is requested, 'False' allows for similar items.
        multiple (BooleanField): Indicates whether multiple instances of this gift are acceptable. Useful for items where having more than one is desirable.
        notes (CharField): Additional notes or details about the gift, can be left blank.
        date_to_remove (DateField): An optional field indicating when this gift should be removed from the list, useful for time-sensitive gifts, and for keeping the list clean once an item is marked as bought. Can be null.
        bought (BooleanField): Indicates whether the gift has been purchased.
        visible_to (ManyToManyField): A list of Members who are allowed to view this gift. This field allows the gift to be visible to specific members, beyond just the gift receiver and adder.

    The 'visible_to' field uses 'related_name' to enable reverse access from Member to view all gifts visible to a particular member using 'Member.visible_gifts.all()'.
    """

    gift_id = models.AutoField(primary_key=True)
    gift_adder = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='adding_gift')
    gift_receiver = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='receiving_gift')
    item_name = models.CharField(max_length=100)
    links = models.ManyToManyField(Link, blank=True)
    exact_item = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    notes = models.CharField(max_length=1000, blank=True)
    date_to_remove = models.DateField(blank=True, null=True, default=None)
    bought = models.BooleanField(default=True)
    visible_to = models.ManyToManyField(Member, related_name='visible_gifts', blank=True)