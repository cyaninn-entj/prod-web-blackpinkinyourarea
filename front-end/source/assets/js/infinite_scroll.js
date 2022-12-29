//IntersectionObserver을 이용한 무한스크롤 구현
const io = new IntersectionObserver((entries, observer) => {
	entries.forEach(entry => {
	  if (!entry.isIntersecting) return; 
		//entry가 interscting 중이 아니라면 함수를 실행하지 않습니다.
	  if (page._scrollchk) return;
		//현재 page가 불러오는 중임을 나타내는 flag를 통해 불러오는 중이면 함수를 실행하지 않습니다.
    observer.observe(document.getElementById('sentinel'));
		//observer를 등록합니다.
    page._page += 1;
		//불러올 페이지를 추가합니다.
    page.list.search();
		//페이지를 불러오는 함수를 호출합니다.
	});
});

io.observe(document.getElementById('sentinel'));



//아이템이 로딩되기 전 UI 구현
$.ajax({
	url: url,
	data: param,
	method: "GET",
	dataType: "json",
	success: function (result) {
	  console.log(result);
	},
	error: function (err) {
	  console.log(err);
	},
	beforeSend: function () {
    _scrollchk = true; 
		//데이터가 로드 중임을 나타내는 flag입니다.
		document.getElementById('list').appendChild(skeleton.show());
		//skeleton을 그리는 함수를 이용해 DOM에 추가해줍니다.
    $(".loading").show();
		//loading animation을 가진 요소를 보여줍니다.
	},
	complete: function () {
    _scrollchk = false;
		//데이터가 로드 중임을 나타내는 flag입니다.
    $(".loading").hide();
    skeleton.hide();
		//loading animation 요소와 skeleton을 지우는 함수를 이용해 DOM에서 지워줍니다.
	}
});



//무한 스크롤 멈추기 구현
if (_total === 0) {
	$('#sentinel').hide();
	//검색된 아이템이 없을 경우 관찰중인 요소를 숨긴다.
}
else {
	if (_total <= _page*20){
		$('#sentinel').hide();
		//검색된 아이템이 20개 이하일 경우 관찰중인 요소를 숨긴다.
	}
	else {
		 $('#sentinel').show();
		//관찰중인 요소를 보여준다.
	}
}


//뒤로 가기 시 이전 스크롤 유지 구현
window.addEventListener('pageshow', function (event) {
	if (event.persisted || window.performance && window.performance.navigation.type == 2) {
		 //
	}
});

if (sessionStorage.getItem("page")) {
    var pageNum = Number.parseInt(sessionStorage.getItem("page"));
    _page = pageNum ;
    list.search();
}