$(function(){

    window.Parsley.addValidator('req',{
        validateString: function(value) {
        return value !== '';
        },
        messages: {       
            en: '%s is required',     
        }
    });
    
    window.Parsley.addValidator('minlen', {
        validateString: function(value,min) {
        return value.length >= min;
        },
        messages: {
            en: 'Min length is %s characters',     
        }
    });

    window.Parsley.addValidator('maxlen', {
        validateString: function(value,max) {
        return value.length <= max;
        },
        messages: {
            en: 'Min length is %s characters',     
        }
    });
    window.Parsley.addValidator('allow', {
        validateString: function(value) {
        return value.toLowerCase() !="admin" && value.toLowerCase() !="user" && value.toLowerCase() != "test";
        },
        messages: {
            en: "Username 'admin' or 'user'or 'test' is not allowed",     
        }
    });

    window.Parsley.addValidator('filerequired', {
        validateString: function(value) {
          return value !== '';
        },
        messages: {
          en: "Avatar is required",
        }
      });

    window.Parsley.addValidator('birthday-min', {
        validateString: function(value) {
            var minDate = new Date('1900-01-01');
            var inputDate = new Date(value);
            return inputDate >= minDate;
        },
        messages: {
            en: "Min birthday is 01/01/1900",
        }
    });


    $('#register-form').parsley().on('form:submit', function() {
        if ($('#register-form').parsley().isValid()) {

            var un = $('#register-form input[name=username]').val();
            var em = $('#register-form input[name=email]').val();
            var pass = $('#register-form input[name=password]').val();


            str='';
            i=0;
            while(i<pass.length){
                str=str+'*'
                i++;
            }

            if(/^\d+$/.test(pass) || /^[a-z]+$/.test(pass) ){
                str +=' (very easy)';
            }
            else if (/^[a-z\d]+$/.test(pass)){
                str+=' (easy)';
            }
            else if (/^[a-z\dA-Z]+$/.test(pass)){
                str+=' (normal)';
            }
            else if (/\d/.test(pass) && /[A-Z]/.test(pass) && /[a-z]/.test(pass) && /[^a-zA-Z0-9]/.test(pass)){
                str+=' (hard)';
            }    

            $('.two:eq(0)').text(un);
            $('.two:eq(1)').text(em);
            $('.two:eq(2)').text(str);

            $('#result').css('display','block');
            $('#register-form').css('display','none');

            return false;
        } 
        else{
            var firstInvalidField = $('#register-form').find('.parsley-error:first');
            if (firstInvalidField.length) {
                firstInvalidField.focus();
            }
        }
    });

 
    $('#save').click(function(){
        
        var full_name = $('#user-info input[name=full-name]').val()
        var avatar = $('#user-info input[name=avatar]').val()
        var birthday = $('#user-info input[name=birthday]').val()
        var gender = $('#user-info input[type=radio]');
        var sub = $('#user-info input[name=subscribe]');
        var g = '';
        gender.each(function() {
            if (this.checked) {
                g = $(this).val();
            }
        });
        var s = sub.prop('checked') ? 'yes' : 'no';
          
        $('.two-info:eq(0)').text(full_name);
        $('.two-info:eq(1)').text(avatar);
        $('.two-info:eq(2)').text(birthday);
        $('.two-info:eq(3)').text(g);
        $('.two-info:eq(4)').text(s);

        $('#user-info').css('display','none');
        $('#result-info').css('display','block');

    })


})

    

