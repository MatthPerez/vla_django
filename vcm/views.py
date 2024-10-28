# import os
# import sys
# from django.conf import settings
# from django.shortcuts import render

# datas_path = os.path.join(settings.STATICFILES_DIRS[0])
# sys.path.append(datas_path)

# from datas.week_meetings import MEETINGS


# def index(request):
#     context = {
#         "date": MEETINGS.date,
#         "president": MEETINGS.president,
#         "prayer1": MEETINGS.prayer1,
#         "prayer2": MEETINGS.prayer2,
#         "song1": MEETINGS.song1,
#         "song2": MEETINGS.song2,
#         "song3": MEETINGS.song3,
#         "portion": MEETINGS.portion,
#         "jewels": MEETINGS.jewels,
#         "jewels_title": MEETINGS.jewels_title,
#         "pearls": MEETINGS.pearls,
#         "reading1": MEETINGS.reading1,
#         "reading2": MEETINGS.reading2,
#         "reading3": MEETINGS.reading3,
#         "alloc1_type": MEETINGS.alloc1_type,
#         "alloc2_type": MEETINGS.alloc2_type,
#         "alloc3_type": MEETINGS.alloc3_type,
#         "alloc4_type": MEETINGS.alloc4_type,
#         "alloc1_duration": MEETINGS.alloc1_duration,
#         "alloc2_duration": MEETINGS.alloc2_duration,
#         "alloc3_duration": MEETINGS.alloc3_duration,
#         "alloc4_duration": MEETINGS.alloc4_duration,
#         "reading_lesson": MEETINGS.reading_lesson,
#         "alloc1_lesson": MEETINGS.alloc1_lesson,
#         "alloc2_lesson": MEETINGS.alloc2_lesson,
#         "alloc3_lesson": MEETINGS.alloc3_lesson,
#         "alloc4_lesson": MEETINGS.alloc4_lesson,
#         "alloc1pupil_hall1": MEETINGS.alloc1pupil_hall1,
#         "alloc1inter_hall1": MEETINGS.alloc1inter_hall1,
#         "alloc2pupil_hall1": MEETINGS.alloc2pupil_hall1,
#         "alloc2inter_hall1": MEETINGS.alloc2inter_hall1,
#         "alloc3pupil_hall1": MEETINGS.alloc3pupil_hall1,
#         "alloc3inter_hall1": MEETINGS.alloc3inter_hall1,
#         "alloc4pupil_hall1": MEETINGS.alloc4pupil_hall1,
#         "alloc4inter_hall1": MEETINGS.alloc4inter_hall1,
#         "alloc1pupil_hall2": MEETINGS.alloc1pupil_hall2,
#         "alloc1inter_hall2": MEETINGS.alloc1inter_hall2,
#         "alloc2pupil_hall2": MEETINGS.alloc2pupil_hall2,
#         "alloc2inter_hall2": MEETINGS.alloc2inter_hall2,
#         "alloc3pupil_hall2": MEETINGS.alloc3pupil_hall2,
#         "alloc3inter_hall2": MEETINGS.alloc3inter_hall2,
#         "alloc4pupil_hall2": MEETINGS.alloc4pupil_hall2,
#         "alloc4inter_hall2": MEETINGS.alloc4inter_hall2,
#         "alloc1pupil_hall3": MEETINGS.alloc1pupil_hall3,
#         "alloc1inter_hall3": MEETINGS.alloc1inter_hall3,
#         "alloc2pupil_hall3": MEETINGS.alloc2pupil_hall3,
#         "alloc2inter_hall3": MEETINGS.alloc2inter_hall3,
#         "alloc3pupil_hall3": MEETINGS.alloc3pupil_hall3,
#         "alloc3inter_hall3": MEETINGS.alloc3inter_hall3,
#         "alloc4pupil_hall3": MEETINGS.alloc4pupil_hall3,
#         "alloc4inter_hall3": MEETINGS.alloc4inter_hall3,
#         "vcm1": MEETINGS.vcm1,
#         "vcm2": MEETINGS.vcm2,
#         "vcm3": MEETINGS.vcm3,
#         "vcm1_duration": MEETINGS.vcm1_duration,
#         "vcm2_duration": MEETINGS.vcm2_duration,
#         "vcm3_duration": MEETINGS.vcm3_duration,
#         "vcm1_title": MEETINGS.vcm1_title,
#         "vcm2_title": MEETINGS.vcm2_title,
#         "vcm3_title": MEETINGS.vcm3_title,
#         "eba": MEETINGS.eba,
#         "eba_reader": MEETINGS.eba_reader,
#         "supervisor": MEETINGS.supervisor,
#         "special_speech": MEETINGS.special_speech,
#     }

#     return render(request, "vcm/index.html", context)


from django.shortcuts import render
from django.views import View


class VcmView(View):
    def get(self, request):
        return render(
            request,
            "vcm/index.html",
        )
