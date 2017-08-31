from django.shortcuts import render
from django.http import HttpResponse
import json
from collections import Counter

# Create your views here.

def users(request):
    video_res = []
    course_res = []
    video_data = {}
    course_data = {}
    with open('static/Tracking-Log.json', 'r') as handle:
        parsed = json.load(handle)
    played_videos = Counter(parsed[i]['username'] for i in range(len(parsed)) if(parsed[i]['username'] != "" and parsed[i]['event_source'] == "browser" and parsed[i]['name'] == "play_video"))
    courses_enrolled = Counter(parsed[i]['username'] for i in range(len(parsed)) if(parsed[i]['username'] != "" and parsed[i]['event_source'] == "server" and parsed[i]['event_type'] == "te.course.enrollment.activated"))
    for k, v in dict(played_videos).items():
        video_data['username'] = k
        video_data['played_videos_count'] = v
        video_res.append(video_data.copy())
    for k, v in dict(courses_enrolled).items():
        course_data['username'] = k
        course_data['enrolled_courses_count'] = v
        course_res.append(course_data.copy())
    return HttpResponse(
            json.dumps({"user_playedvideo's_count": video_res, "user_enrolled_courses": course_res}),
            content_type="application/json"
        )
