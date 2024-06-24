import functions_framework
@functions_framework.http
def hello_http(request):
    data_received=request.form("text_from_user")
    #porcess
    data_to_send="processed data"
    return data_to_send
    
