$(document).ready(function(){
    let spinner = $('.spinner').addClass('hide')
    let no_post_alert = $('.no-post-alert').addClass('hide')

    $('.load-btn').click(function(){
        let current_post = $('.single-post-box').length;
        let total_post = $(this).attr('data-total');
        
        $.ajax({
            url:'/load-post',
            type:'GET',
            data:{
                post:current_post
            },
            dataType:'json',
            beforeSend:function(){
                console.log('wait')
                spinner.removeClass('hide')
                $('.load-btn').attr('disabled',true)
            },
            success:function(res){
                spinner.addClass('hide')
                $('.load-btn').attr('disabled',false)
                $('.all-posts-container').append(res.blog_posts)

                let current_post = $('.single-post-box').length;
                if(current_post==total_post){
                    no_post_alert.removeClass('hide')
                    $('.load-btn').remove()
                }
            },
            error:function(err){
                console.log(err)
            }

        })
    })

})
