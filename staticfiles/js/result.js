/////// URL 복사 코드 ////////

const copyBtn = document.querySelector('.copy_btn');

/* clipboard api를 사용한 클립보드 복사 */
function copyUrl() {
    const url = 'https://fbti-eizsr.run.goorm.site/';

    navigator.clipboard.writeText(url).then(() => {
        alert("URL이 복사되었습니다"); 
    });
}

copyBtn.addEventListener('click', copyUrl);


/////// URL 복사 코드 끝 ////////