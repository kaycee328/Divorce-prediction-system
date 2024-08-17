from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from enum import Enum


class Rating(Enum):
    VERY_BAD = 0
    BAD = 1
    NEUTRAL = 2
    GOOD = 3
    VERY_GOOD = 4


class DPS(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    divorce_status = models.BooleanField(default=False, null=True)
    n1 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="When one of you apologizes after a discussion goes in a bad direction, does it extend?",
    )

    n2 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you ignore each other's differences at the end of the day?",
    )

    n3 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you and your partner take discussions to correct your issues?",
    )

    n4 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you and your partner contact each other after an argument?",
    )

    n5 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Is time spent with your partner special?",
    )

    n6 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you have time for each other at home?",
    )

    n7 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Are you and your partner like strangers at home?",
    )

    n8 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you enjoy holidays with your partner?",
    )

    n9 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you enjoy travelling with your partner?",
    )

    n10 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you and your partner have similar goals?",
    )

    n11 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you think that you and your partner can live in harmony?",
    )

    n12 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you and your partner have similar values in terms of personal freedom?",
    )

    n13 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you both have similar goals for your children or friends?",
    )

    n14 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you both have similar dreams on how you want to live?",
    )

    n15 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do the both of you have similar ideas on what love should be?",
    )

    n16 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you share the same views about being happy in life?",
    )

    n17 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you have similar ideas on what marriage should be?",
    )

    n18 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you have similar ideas about how roles should be in marriage?",
    )

    n19 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do the both of you have similar values in trust?",
    )

    n20 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know what your partner likes?",
    )

    n21 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know how to take care of your partner when they are sick?",
    )

    n22 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know your partner's favourite meal?",
    )

    n23 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Can you tell when your partner is stressed?",
    )

    n24 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you have knowledge of your partner's inner world?",
    )

    n25 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know your partner's basic concerns?",
    )

    n26 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know what stresses your partner?",
    )

    n27 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know your partner's hopes and wishes?",
    )

    n28 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know your partner very well?",
    )

    n29 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you know your partner's friend circle?",
    )

    n30 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you feel aggressive when you argue with your partner?",
    )

    n31 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="When discussing with your partner do you use vulgar expressions?",
    )

    n32 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Can you use negative statements about your partner's personality during your discussions?",
    )

    n33 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Can you use offensive expressions during your discussions?",
    )

    n34 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Can you insult your partner during your discussions?",
    )

    n35 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you humiliate your partner when you argue?",
    )

    n36 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Is your argument with your partner calm?",
    )

    n37 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you hate your partner's way of bringing things up?",
    )

    n38 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you and your partner fight during arguments?",
    )

    n39 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Are you and your partner already fighting before you know what's going on?",
    )

    n40 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you lose your calm when talking to your partner about something?",
    )

    n41 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="When you and your partner are arguing, do you say a word?",
    )

    n42 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Are you mostly thirsty to calm the environment?",
    )

    n43 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you think it's good for you to leave home for a while?",
    )

    n44 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Would you rather stay silent than argue with your partner?",
    )

    n45 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Even if you are right in the argument, are you thirsty to upset the other side?",
    )

    n46 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="When you argue with your partner, do you remain silent because you are afraid of not being able to control your anger?",
    )

    n47 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you feel like you are right during your discussions with your partner?",
    )

    n48 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Do you have anything to do with what your partner accused you of?",
    )

    n49 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Are you the one who is wrong about the problems at home?",
    )

    n50 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Would you hesitate to tell anyone about your partner's inadequacies?",
    )

    n51 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="When you discuss your partner, do you tell people about their inadequacies?",
    )

    n52 = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        error_messages={
            "min_value": "The value must be within the range of 0-4",
            "max_value": "The value must be within the range of 0-4",
            "invalid": "Please enter a valid integer.",
        },
        verbose_name="Lastly, are you afraid of telling people about your partner's inadequacies?",
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        user = self.user
        divorce_status = self.divorce_status

        if divorce_status == True:
            status = "Divorced"
        else:
            status = "Not Divorced"

        return f"Username: {str(user).upper()} || Divorce Status: {str(status).upper()}"

    def save(self, *args, **kwargs):
        # Perform your calculation here and set divorce_status
        def some_calculation():
            pass

        # Example calculation:
        self.divorce_status = self.some_calculation()

        # Call the parent class's save method to save the object to the database
        super().save(*args, **kwargs)
