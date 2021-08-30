/*카카오톡 공유js코드*/

function kakaoShare(){
  Kakao.Link.sendDefault({
      objectType: 'feed',
      content: {
        title: '오늘 이거 먹어!',
        description: '오늘 뭐먹지 고민된다면? 대신 골라드려요',
        imageUrl:
          'img/mobile.jpg',
        link: {
          mobileWebUrl: 'https://eat-this.netlify.app/',
          androidExecutionParams: 'test',
        },
      },
      social: {
        likeCount: 188,
        commentCount: 71,
        sharedCount: 208,
      },
      buttons: [
        {
          title: '웹으로 이동',
          link: {
            mobileWebUrl: 'https://eat-this.netlify.app/',
          },
        },
        {
          title: '앱으로 이동',
          link: {
            mobileWebUrl: 'https://eat-this.netlify.app/',
          },
        },
      ]
    });
  }  