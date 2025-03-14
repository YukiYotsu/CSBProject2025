from django.shortcuts import render
from .models import Vote
from django.http import HttpResponse
from django.db import connection

def vote_management(request):
    votes = Vote.objects.all()
    return render(request, 'vote/vote_management.html', {'votes': votes})

# 修正: アクセス制限を追加する
# from django.contrib.auth.decorators import login_required

# @login_required
# def vote_management(request):
#     votes = Vote.objects.all()
#     return render(request, 'vote/vote_management.html', {'votes': votes})

def vote_form(request):
    if request.method == "POST":
        vote_choice = request.POST.get("vote_choice")
        
        # SQLインジェクションの脆弱性
        query = f"SELECT * FROM vote_choice WHERE choice_name = '{vote_choice}'"
        cursor = connection.cursor()
        cursor.execute(query)

        # 投票結果をクライアント側で直接処理（改ざん可能）
        return HttpResponse(f"投票しました: {vote_choice}")
    return render(request, 'vote/vote_form.html')

# 修正: サーバー側で投票データを処理
# def vote_form(request):
#     if request.method == "POST":
#         vote_choice = request.POST.get("vote_choice")
#         # サーバー側で投票結果を管理
#         return HttpResponse(f"投票しました: {vote_choice}")
#     return render(request, 'vote/vote_form.html')
