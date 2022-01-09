from .models import Admin, Staff, Student, User


def user(request):
    try:
        user = User.objects.get(username=request.user)
        usertype = None
        if user:
            try:
                usertype = Admin.objects.get(user=user)
            except Admin.DoesNotExist:
                usertype = None
            
            try:
                usertype = Student.objects.get(user=user)
            except Student.DoesNotExist:
                pass
            
            try:
                usertype = Staff.objects.get(user=user)
            except Staff.DoesNotExist:
                pass
            
            return {
                'usertype': usertype,
            }
    except User.DoesNotExist:
        return {'usertype': False}
