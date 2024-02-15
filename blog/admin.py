from django.contrib import admin
from .models import Art , Category
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.
@admin.action(description="نمایش دسته یندی های انتخاب شده")
def cat_publish(modeladmin,request,queryset):
    updated = queryset.update(status=True)
    modeladmin.message_user(request,ngettext(
        "%d  دسته بندی نمایش داده خواهد شد",
        "%d تا دسته بندی نمایش داد خواهد شد",
        updated,
            )
        % updated,
            messages.SUCCESS,
    )

@admin.action(description="عدم نمایش دسته یندی های انتخاب شده")
def cat_draft(modeladmin,request,queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(request,ngettext(
        "%d  دسته بندی نمایش داده نخواهد شد",
        "%d تا دسته بندی نمایش داد نخواهد شد",
        updated,
            )
        % updated,
            messages.SUCCESS,
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields ={'slug': ('title',)}
    actions =[cat_publish ,cat_draft]

admin.site.register(Category,CategoryAdmin)



@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(request,ngettext(
        "%d مقاله منشر شد و در سایت نمایش داده خواهد شد",
        "%d تا مقاله منتشر شده و در سایت نمایش داد خواهد شد",
        updated,
            )
        % updated,
            messages.SUCCESS,
        )



@admin.action(description="پیش نویس مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(request,ngettext(
        "%d مقاله پیش نویس شده و دیگر در سایت نمایش داده نخواهد شد  ",
        "%d تا مقاله پیش نویس شد و دیگر در سایت نمایش داده نخواهد شد ",
        updated,
            )
        % updated,
            messages.SUCCESS,
        )


class ArtAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','author','jpublish','status','category_to_str')
    list_filter = ('publish','status','author')
    search_fields = ('title','description')
    prepopulated_fields ={'slug': ('title',)}
    ordering = ['-status','-publish']
    actions = [make_published , make_draft]

   
admin.site.register(Art,ArtAdmin)
