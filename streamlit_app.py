import streamlit as st

st.title("文脈推定デモ（A例文）")

st.subheader("例文")
st.write(
    "洗剤を買ってきてと頼まれたので買ってきて渡したら、相手は不服そうにしていた。"
)

stage = st.selectbox(
    "推論レベルを選択",
    ["Stage1-2（従来AI）", "Stage3", "Stage4", "Stage5"]
)

st.subheader("解釈")

if stage == "Stage1-2（従来AI）":
    st.write(
        "- 洗剤を購入したという事実\n"
        "- 相手が不満そうだったという結果\n"
        "- 不満の理由は特定できない"
    )

elif stage == "Stage3":
    st.write(
        "- 相手は特定の種類の洗剤を想定していた可能性\n"
        "- その意図は事前に共有されていない"
    )

elif stage == "Stage4":
    st.write(
        "- 期待と結果の不一致が不満の原因\n"
        "- 買ってきた側に過失はない"
    )

elif stage == "Stage5":
    st.write(
        "- 文脈共有不足による認知のズレ\n"
        "- 暗黙の前提が破綻した典型例"
    )