from os import path

debug = path.exists('./.dev')
# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_host = '0.0.0.0' # dev
app_port = 8081 # dev
app_name = 'Borocol'
app_path = path.dirname(__file__)
# api
api_prefix = '/api/v1'
# request
request_maxContentLength = 16 * 1024 * 1024 # 16m MAX_CONTENT_LENGTH
# file
file_uploadDir = path.join(app_path, 'uploads')
file_allowedExtensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'])
#
file_fields = {
    'course_detail': ['photos'],
    'accomodation_detail': ['instructor_photo', 'cover', 'photos'],
    'student_profile': ['avatar']
}
