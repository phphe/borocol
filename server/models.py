from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table
from cassandra.cqlengine.models import Model


class user(Model):

    id      = columns.UUID(required=True, primary_key=True)

    password      = columns.Text(required=False, )

    privacy      = columns.Text(required=False, )

    email      = columns.Text(required=False, )

    user_type      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_subscriptions(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    require_accomodation      = columns.Text(required=False, )

    require_insurance      = columns.Text(required=False, )

    payment_details      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class school_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    contact_persons      = columns.Text(required=False, )

    school_name      = columns.Text(required=False, )

    registration_document      = columns.Text(required=False, )

    stripe_details      = columns.Text(required=False, )

    address1      = columns.Text(required=False, )

    address2      = columns.Text(required=False, )

    city      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    introduction      = columns.Text(required=False, )

    logo      = columns.Text(required=False, )

    school_photos      = columns.Text(required=False, )

    subscriptions      = columns.Text(required=False, )

    website      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class student_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    frist_name      = columns.Text(required=False, )

    last_name      = columns.Text(required=False, )

    phone_number      = columns.Text(required=False, )

    gender      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    currency      = columns.Text(required=False, )

    language      = columns.Text(required=False, )

    passport_information      = columns.Text(required=False, )

    liked_courses      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_detail(Model):

    id      = columns.UUID(required=True, primary_key=True)
    school_id      = columns.Text(required=False, )

    name = columns.Text(required=True, )
    category_id = columns.Text(required=True, )
    level = columns.Text(required=True, )
    start_date = columns.DateTime(required=True, )
    end_date = columns.DateTime(required=True, )
    description = columns.Text(required=False, )
    group_size = columns.Integer(required=True, )
    gender = columns.Text(required=False, )
    age_range = columns.List(columns.Integer, required=False, )
    hours = columns.Integer(required=True, )
    language = columns.Text(required=True, )
    instructor_photo = columns.Text(required=False, )
    instructor_info = columns.Text(required=False, )
    issue_certificate = columns.Boolean(required=True, )
    certificate = columns.Text(required=False, )
    address = columns.Text(required=True, )
    city = columns.Text(required=True, )
    country = columns.Text(required=True, )
    api_key = columns.Text(required=True, )
    location_description = columns.Text(required=False, )
    how_to_get_there = columns.Text(required=False, )
    where_to_meet = columns.Text(required=False, )
    schedule = columns.Text(required=True, )
    meals_included = columns.Boolean(required=True, )
    meals = columns.List(columns.Text, required=False, )
    meals_info = columns.Text(required=False, )
    provide = columns.Text(required=False, )
    guest_needs_to_bring = columns.Text(required=False, )
    guest_requirement = columns.Text(required=False, )
    request_form_existed = columns.Boolean(required=True, )
    request_form = columns.Text(required=False, )
    tags = columns.List(columns.Text, required=False, )
    cover = columns.Text(required=True, )
    photos = columns.List(columns.Text, required=True, )
    notes = columns.Text(required=False, )
    seats = columns.Integer(required=True, )
    price = columns.Decimal(required=True, )
    registration_start_date = columns.DateTime(required=True, )
    registration_end_date = columns.DateTime(required=True, )
    early_bird_discount = columns.Boolean(required=False, )
    discount_rate = columns.Text(required=False, )
    quota = columns.Text(required=False, )
    down_payment = columns.Boolean(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class accomodation_detail(Model):

    id      = columns.UUID(required=True, primary_key=True)
    course_id      = columns.Text(required=False, )

    options = columns.List(columns.Text, required=False, )
    other_options = columns.Text(required=False, )
    location_description = columns.Text(required=False, )
    facilities = columns.List(columns.Text, required=False, )
    other_facilities = columns.Text(required=False, )
    photos = columns.List(columns.Text, required=False, )
    room1_enabled = columns.Boolean(required=False, )
    room1_type = columns.Text(required=False, )
    room1_quota = columns.Text(required=False, )
    room1_price = columns.Text(required=False, )
    room2_enabled = columns.Boolean(required=False, )
    room2_type = columns.Text(required=False, )
    room2_quota = columns.Text(required=False, )
    room2_price = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class visa_detail(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    information      = columns.Text(required=False, )

    last_date_submission      = columns.Text(required=False, )

    document_description      = columns.Text(required=False, )

    visa_url      = columns.Text(required=False, )

    schooli_invitation_letter      = columns.Text(required=False, )

    refund_policy      = columns.Text(required=False, )

    auto_reply_message      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class featured_course(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class reviews(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    ratings      = columns.Text(required=False, )

    comments      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_types(Model):

    id      = columns.UUID(required=True, primary_key=True)

    name      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    description      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class test(Model):

    id      = columns.UUID(required=True, primary_key=True)
    ls      = columns.List(columns.Text, required=False, )
    lsi      = columns.List(columns.Integer, required=False, )
    dm      = columns.Decimal(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

# this func will auto create tables
# coonect database before do this
def sync_tables():

  sync_table(user)

  sync_table(course_subscriptions)

  sync_table(school_profile)

  sync_table(student_profile)

  sync_table(course_detail)

  sync_table(accomodation_detail)

  sync_table(visa_detail)

  sync_table(featured_course)

  sync_table(reviews)

  sync_table(course_types)

  sync_table(test)
