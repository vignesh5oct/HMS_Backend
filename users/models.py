from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("full name"), max_length=150)
    dob = models.DateField(_("date of birth"), null=True, blank=True)
    phone = models.CharField(_("phone number"), max_length=10, blank=True)
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES, blank=True)
    
    profile_photo = models.ImageField(_("profile photo"), upload_to='profile_photos/', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='doctor_profile')

    # Registration
    is_registered = models.BooleanField(_("is registered"), default=False)
    register_years = models.PositiveIntegerField(_("years registered"), null=True, blank=True)

    # Address
    address = models.CharField(_("clinic address"), max_length=255, blank=True)
    address2 = models.CharField(_("address line 2"), max_length=255, blank=True)
    zipcode = models.CharField(_("pincode/zipcode"), max_length=10, blank=True)

    # Certification uploads
    qualification_certificate = models.FileField(upload_to="certificates/", null=True, blank=True)
    photo_id = models.FileField(upload_to="ids/", null=True, blank=True)
    clinical_employment = models.FileField(upload_to="employment_docs/", null=True, blank=True)

    # Physical info
    weight = models.DecimalField(_("weight"), max_digits=5, decimal_places=2, null=True, blank=True)
    weight_unit = models.CharField(max_length=10, default="kg")

    height = models.DecimalField(_("height"), max_digits=5, decimal_places=2, null=True, blank=True)
    height_unit = models.CharField(max_length=10, choices=[("cm", "cm"), ("ft", "ft")], default="cm")

    age = models.PositiveIntegerField(_("age"), null=True, blank=True)

    BLOOD_GROUP_CHOICES = [
        ("A-", "A-"), ("A+", "A+"),
        ("B-", "B-"), ("B+", "B+"),
        ("AB-", "AB-"), ("AB+", "AB+"),
        ("O-", "O-"), ("O+", "O+"),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)

    # Location
    city = models.CharField(_("city"), max_length=100, blank=True)
    state = models.CharField(_("state"), max_length=100, blank=True)

    # Optional additional fields
    specialization = models.CharField(_("specialization"), max_length=100, blank=True)
    experience_years = models.PositiveIntegerField(_("years of experience"), default=0)
    bio = models.TextField(_("biography"), blank=True)

    def __str__(self):
        return f"{self.user.email} - Profile"



class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='patient_profile')
   
    BLOOD_GROUP_CHOICES = [
        ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'),
        ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+'),
    ]

    HEIGHT_UNIT_CHOICES = [('cm', 'cm'), ('ft', 'ft')]
    WEIGHT_UNIT_CHOICES = [('kg', 'kg')]

    # Step 2: Personal Details
    is_pregnant = models.BooleanField(default=False)
    pregnancy_term = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    weight_unit = models.CharField(max_length=3, choices=WEIGHT_UNIT_CHOICES, default='kg')
    height = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    height_unit = models.CharField(max_length=3, choices=HEIGHT_UNIT_CHOICES, default='cm')
    age = models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True, blank=True)
    heart_rate = models.CharField(max_length=10,null=True, blank=True)
    bp = models.CharField(max_length=10,null=True, blank=True)
    glucose = models.CharField(max_length=10,null=True, blank=True)
    allergies = models.TextField(blank=True, null=True)

    has_conditions = models.BooleanField(default=False)
    conditions = models.JSONField(blank=True, null=True)

    takes_medicine = models.BooleanField(default=False)
    medicines = models.JSONField(blank=True, null=True)

    # Step 3: Covered Members
    self_covered = models.BooleanField(default=True)
    spouse_covered = models.BooleanField(default=False)
    child_count = models.IntegerField(default=0)
    mother_covered = models.BooleanField(default=False)
    father_covered = models.BooleanField(default=False)

    # Step 4: Family Member Details
    child_1_age = models.IntegerField(blank=True, null=True)
    child_1_image = models.ImageField(upload_to='patient_docs/', blank=True, null=True)

    spouse_age = models.IntegerField(blank=True, null=True)
    spouse_file = models.ImageField(upload_to='patient_docs/', blank=True, null=True)

    father_age = models.IntegerField(blank=True, null=True)
    father_file = models.ImageField(upload_to='patient_docs/', blank=True, null=True)

    mother_age = models.IntegerField(blank=True, null=True)
    mother_file = models.ImageField(upload_to='patient_docs/', blank=True, null=True)

    # Step 5: Location
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"PatientProfile ({self.gender}, Age: {self.age})"