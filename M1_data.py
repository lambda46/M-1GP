import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px



judge_dict = {2001: ['きよし', '青島', '小朝', '石井', '鴻上', '松本', '紳助'],
            2002: ['談志', 'カウス', '洋七', '石井', '大竹', '松本', '紳助'],
            2003: ['カウス', '大竹', '石井', '洋七', '南原', '松本', '紳助'],
            2004: ['カウス', '石井', '小朝', '洋七', '大竹', '南原', 'きよし'],
            2005: ['カウス', '石井', '洋七', '大竹', '渡辺', '松本', '紳助'],
            2006: ['カウス', '大竹', '洋七', '渡辺', '南原', '松本', '紳助'],
            2007: ['カウス', '大竹', '巨人', '石井', '上沼', '松本', '紳助'],
            2008: ['カウス', '大竹', '巨人', '渡辺', '上沼', '松本', '紳助'],
            2009: ['カウス', '渡辺', '巨人', '東国原', '上沼', '松本', '紳助'],
            2010: ['カウス', '宮迫', '渡辺', '大竹', '南原', '松本', '紳助'],
            2015: ['哲夫', '佐藤', '石田', '富澤', '徳井', '吉田', '岩尾', '増田', '礼二'],
            2016: ['巨人', '礼二', '大吉', '松本', '上沼'],
            2017: ['巨人', '渡辺', '礼二', '小朝', '大吉', '松本', '上沼'],
            2018: ['巨人', '礼二', '塙', '志らく', '富澤', '松本', '上沼'],
            2019: ['巨人', '塙', '志らく', '富澤', '礼二', '松本', '上沼'],
            2020: ['巨人', '富澤', '塙', '志らく', '礼二', '松本', '上沼'],
            2021: ['巨人', '富澤', '塙', '志らく', '礼二', '松本', '上沼'],
            2022: ['邦子', '大吉', '塙', '富澤', '志らく', '礼二', '松本'],
            2023: ['邦子', '大吉', '富澤', '塙', 'ともこ', '礼二', '松本']}

year_list = list(range(2001, 2011))+list(range(2015, 2024))

m1_score = pd.read_csv("M-1/得点/1st得点.csv")
m1_result = pd.read_csv("M-1/結果/決勝戦結果.csv")

st.set_page_config(layout='wide')
st.title("M-1グランプリ 歴代1stラウンド得点")

cols = st.columns(7)
with cols[0]:
    year = st.selectbox(
        "開催年",
        ["通算"] + year_list,
        index=0
    )
if year == "通算":
    df = m1_score
    st.dataframe(df, use_container_width=True)

else:
    judge_name = judge_dict[year]
    judge_div = [s+"_偏差値" for s in judge_dict[year]]
    judge_cols = [x for pair in zip(judge_name, judge_div) for x in pair]
    df = m1_score[m1_score["年"] == year][["年", "出番順", "コンビ名", "合計得点", "平均点", "偏差値"] + judge_cols].reset_index(drop=True)
    styled_data = (
        df.style
        .background_gradient(cmap="coolwarm", subset=["合計得点", "平均点"] + judge_name)
        .background_gradient(cmap="coolwarm", subset=["偏差値"] + judge_div, vmin=0, vmax=100)
        .format({
            "合計得点": "{:.0f}",  # "合計得点"を整数表示に設定
            "平均点": "{:.1f}",    # "平均点"を小数点1桁に設定
            "偏差値": "{:.1f}",     # "偏差値"を小数点1桁に設定
            **{col: "{:.1f}" for col in judge_div},
            **{col: "{:.0f}" for col in judge_name}
        })
    )
    st.dataframe(styled_data)