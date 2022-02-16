
$(document).ready(function() {
    $('#region').change(function() {
        if($(this).val() == 'Scotland') {
            var TransArr = [132,220,275,400];
            for(var i = 0; i < TransArr.length; i++){
                $('#transmission').append('<option ' + 'value="' + TransArr[i] + '"' + '>' + TransArr[i] + '</option>')
            }
            var DisArr = [11,33,66];
            for(var i = 0; i < DisArr.length; i++){
                $('#distribution').append('<option ' + 'value="' + DisArr[i] + '"' + '>' + DisArr[i] + '</option>')
            }
            return;
        }else{
            var TransArr = [220,275,400];
            for(var i = 0; i < TransArr.length; i++){
                $('#transmission').append('<option ' + 'value="' + TransArr[i] + '"' + '>' + TransArr[i] + '</option>')
            }
            var DisArr = [11,33,66,132];
            for(var i = 0; i < DisArr.length; i++){
                $('#distribution').append('<option ' + 'value="' + DisArr[i] + '"' + '>' + DisArr[i] + '</option>')
            }
        }
    });
});
