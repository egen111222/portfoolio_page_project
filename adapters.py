from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField

class ImageView(ModelView):
    form_extra_fields = {
        'img': ImageUploadField(base_path="static")
    }
