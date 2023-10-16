var confirmDelete = (function (element) {
    var className = element.className;
    if (className.indexOf('need-to-confirm') > -1) {
        element.className = className.replace('need-to-confirm', 'confirmed');
        return false;
    } else {
        element.remove();
    }
});