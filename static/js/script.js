
$(document).ready(function () {
    alert('Script is executed!');
    $('.datetimepicker-input').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',  // Specify the desired date and time format
    });
});
