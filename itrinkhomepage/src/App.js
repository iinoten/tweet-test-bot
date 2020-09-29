import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="page_title">
        <div>ニュースアドバイザー「ITrink」とは</div>
      </div>
      <div className="first_content">
        ITrinkは、SNSでのうその情報やフェイクニュースが広まることを防ぐことを目的に作られたサービスです。
        <br/><br/>Twitterでたくさんの人に見られている投稿を見つけ、内容が危険なものではないかの判断を自動で分析しTwitterを使う人たちがわかりやすいように表示します。
      </div>
      <div className="second_content">
        <div className="second__content__title">ITrinkについて</div>
        <div className="q_and_a_content">
          <div className="Itrink_q">・ITrinkがみつける投稿は内容が怪しいものということですか？</div>
          <div className="Itrink_a">いいえ、ITrinkがみつけるのは「これからたくさんの人に見られるかもしれない投稿」です。<br />
            ITrinkがみつけるものがフェイクニュースやデマときまっているわけではありません。</div>
        </div>

        <div className="Itrink_q">・ITrinkはどうやって真偽の分析をしているんですか？</div>
        <div className="Itrink_a">Twitterにある、過去たくさんの人の目に触れた投稿や誰かに見せたくなる文章の書きかたを参考にみつけた投稿を分析しています。<br/>
          また、内容がきちんとほんとうかどうかを調べその結果も含めた分析結果を点数にして表示して
          います。</div>
        <div className="Itrink_q">・ITrinkがつける点数はどのようにみればいいですか</div>
        <div className="Itrink_a">
          ITrinkがつける点数はあくまでも目安です。<br/>
          高い点数だから信じられる内容である。低い点数なので嘘の情報であるといった
          判断はしないようにしてください。<br/>判断基準のひとつとしてみていただくと幸いです。</div>
      </div>
      <div className="second_content">
        <div className="second__content__title">ITrinkが作られた理由</div>
        <div className="first_content">
          ITrinkはCode for Japan主催の「社会問題解決のサービス開発コンテスト Civitech Challenge Cup U22」の
          に出場するチーム「itrink」によって開発されています。コロナ禍でSNS上の様々な憶測や情報が飛びかう中、
          情報の真偽を確かめる材料が増えることがSNSユーザーに情報のチェックを促すことに繋がり、情報に錯そうされることを防ごうという理念の元つくられています。
        </div>
        </div><div className="second_content">
          <div className="second__content__title">リンク</div>
          <div className="first_content">
            <div className="top-link">
              <a href="https://twitter.com/rumor_check">ITrink Twitter</a>
            </div>
            <div className="link">
              <a href="https://ccc2020.code4japan.org/">CivitechChallengeCup[U-22]<br /></a>
            </div>
          </div>
        </div>

    </div>
  );
}

export default App;
