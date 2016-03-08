var input = '<div class="edit-panel">\
                <textarea name="comment" class="edit-input form-control" rows="4" style="resize:none;"></textarea>\
                 <p style="margin-top:20px;text-align:center;">\
                    <button class="cancel_update btn btn-danger" style="margin-left:10px;width:40%;">Cancelar</button>\
                    <button class="send_update btn btn-primary" style="margin-left:10px;width:40%;">Enviar</button>\
                 </p>\
             </div>';
    
    
function setEditable(button, token){
    url = button.data('url');
    element = button.parents('.content').find('.edit_area');
    element.hide().after(input);
    
    content = element.html();
    
    $('.edit-input').val(content);
    $('.comment-actions').parent().fadeOut();
    

    $('.send_update').on('click', function(){
        if($('.edit-input').val()===''){
            return false;
        }

        $.ajax(url,{
            method: 'POST',
            data: {'comment':$('.edit-input').val(), 'csrfmiddlewaretoken': token},
            success: function(response){
                element.html(response);
                $('.edit-panel').detach();
                element.fadeIn();
                $('.comment-actions').parent().fadeIn();
            },
            error: function(){
                element.siblings('.alert').remove()
                element.before('<p class="alert alert-danger fade in">Ha ocurrido un error, por favor intenta nuevamente</p>');
            }
        });
    });

    $('.cancel_update').on('click', function(){
        $('.edit-panel').detach();
        element.fadeIn();
        $('.comment-actions').parent().fadeIn();
        $('.alert').remove();
    });
};