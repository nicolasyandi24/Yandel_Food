function redireccionar(url,id) {
    window.location.href=url+"/"+id;
}

function volver(url) {
    document.location.href="{% url '"+url+"' %}"
}