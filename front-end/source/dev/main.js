var loading = false;    //중복실행여부 확인 변수
var page = 1;   //불러올 페이지

/*nextpageload function*/
function next_load()
{
        $.ajax({
                type:"GET",
                url:"/test.php",
                data : {'page':page},
                dataType : "text",
                success: function(string)
                {
                    if(string=='success')
                    {
                        console.log(page+' page load');
                        /* 이미지 동적 추가 */
                        for (var x=1;x<6;x++)   
                        {
                            var append_node = "";
                            append_node += "<div class='img_box fadein'>";
                            append_node += "<div class='img_text'>이 이미지는 "+(page*5+x)+"번째 이미지입니다.</div>";
                            append_node += "<img class='test_image' src='//encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRV6cQWlpzaeM-IwJoGf1upU36c_ya_heQdlLRuUgrQqY8GbRFB&usqp=CAU'>";
                            append_node +="</div>";
                            $('body').append(append_node)
                        }
                        page++; //페이지 증가
                        loading = false;    //실행 가능 상태로 변경
                    }
                    else
                    {
                        alert('failed');
                    }
                }
                ,error: function(xhr, status, error) 
                {
                    alert(error);
                }
            });
}

$(window).scroll(function(){
    if($(window).scrollTop()+200>=$(document).height() - $(window).height())
    {
        if(!loading)    //실행 가능 상태라면?
        {
            loading = true; //실행 불가능 상태로 변경
            next_load(); 
        }
        else            //실행 불가능 상태라면?
        {
            alert('다음페이지를 로딩중입니다.');  
        }
    }
});