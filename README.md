# 胡俊杰 / Junjie Hu — Academic Homepage

中英文静态学术主页，保留现有 GitHub Pages 地址：
- English: https://junjiehu-traffic.github.io/junjiehuits/frontend/
- 中文: https://junjiehu-traffic.github.io/junjiehuits/frontend/index_cn.html

## 使用与维护

页面无需 Node.js、npm、React 或在线 API，即可由 GitHub Pages 直接提供。
双击 frontend/index_cn.html 或 frontend/index.html 可浏览；完整预览建议：

```powershell
python -m http.server 8765 --directory frontend
```

访问 http://127.0.0.1:8765/index_cn.html 。

- 双语论文、简介、经历和既有荣誉：frontend/data/content.json。
- 更新日期：同一 JSON 中的 updated 字段；这是内容更新日期，不是访问当天日期。
- 双语界面文字、研究方向介绍和动态：scripts/build.py 的 UI 字典。
- 样式：frontend/css/style.css；交互：frontend/js/main.js。
- 修改内容后运行 python scripts/build.py，同时重新生成两种语言的静态 HTML。
- 保留 frontend 路径，以兼容现有公开 URL。发布时将完整文件树提交至原仓库 main 分支，继续使用其现有 GitHub Pages 配置。

## 本次改版

- 参考 [Anleeno Academic](https://github.com/Anleeno/anleeno-academic) 的双栏结构、淡紫色调、论文图文条目和时间线，使用独立静态实现；未复用参考作者的照片、身份信息、论文或品牌素材。
- 中英文同步新增：2026 年 10 月入选中国科协青年科技人才培育工程博士生专项计划。入选事实与月份来自网站所有者本次提供的信息；未将官方计划管理办法当作个人入选公示。
- 更新日期为 2026-11-12。
- 论文默认按四个研究方向分组展示，各组都有独立标题和篇数，组内按发表年份倒序排列，同一年内按已记录的发表日期倒序。支持方向/年份/关键词联合筛选、研究概览、原始图示、引用复制、筛选状态随语言切换保留；筛选时隐藏无匹配论文的分组并更新组内计数，清除筛选后恢复四组完整列表。未启用 JavaScript 时也能直接阅读全部四组。
- 支持明暗主题、移动端导航、键盘焦点、Escape 关闭弹窗、减少动画偏好、打印布局。
- 页面正文直接写入 HTML；JavaScript 不可用时论文及贡献仍可阅读。
- 既有 PDF 简历 JunjieHu_CV.pdf 保留原文件；本次新增荣誉更新在网页中。

## 内容与核验记录

原站源码基线：5bdc18b025fa60e5afb0f194eea5143ee8e34de1。
第二轮修订（2026-11-12）：简介正文由 14px 调整为桌面 18px、手机 16px；论文标题为 18px，并同步增大作者、元数据和控件文字，调整留白。简介及硕士经历补充导师 Jaeyoung Jay Lee（按出版记录核对姓名拼写）。科协荣誉改为普通条目，动态中也不作特殊高亮。

分类统一为“交通时空数据建模”（4 篇）、“交通安全”（4 篇）、“驾驶行为”（5 篇）与“其他研究尝试”（3 篇）。保留既有 14 项并增加 2 项，共 16 篇。按研究的主要对象和任务归类：ID 3（PST-CGCN 区域事故风险预测）与 ID 4（Tucker-Net/SIRS 事故动态关联）并入交通时空数据建模；机场接客区安全、两篇 K-car 严重程度分析及 BRACE 归入交通安全；跟驰、轨迹网络、驾驶风格及残差学习归入驾驶行为；道路网络形态、动态分区和公共电动汽车充电保留在其他研究尝试。论文元数据、研究概述和图示未因分类调整而改动。

### 论文元数据核验与修订

2026-11-12 依据出版社公开页面及出版社提交至 Crossref 的记录，核对全部 16 篇的题目、作者顺序、DOI、期刊和卷期信息。`frontend/data/content.json` 各项的 `verification.source` 保存可查询的原始元数据端点；`id` 沿用原站序号，15、16 为本次新增。未声称逐篇阅读全文。

| ID | DOI | 主要处理 |
| --- | --- | --- |
| 1 | 10.1016/j.chaos.2024.114965 | 核对题目、作者，补卷号与文章号 |
| 2 | 10.1177/03611981261419011 | 补 DOI；作者改为 Hu、Lee、Bai、Mao；2680(11), 153–173 |
| 3 | 10.1016/j.eswa.2024.125315 | 题目补回 Granger 等正式措辞；正式卷期年份改为 2025 |
| 4 | 10.1016/j.jfranklin.2025.107946 | 校正作者顺序并补 Byon；补卷期信息 |
| 5 | 10.1109/TITS.2023.3316199 | 将错误 DOI 尾号 3275986 改为 3316199；正式卷期为 2024 |
| 6 | 10.1080/15389588.2025.2571048 | 校正作者顺序并补 Kim；2025 在线、2026 正式卷期 |
| 7 | 10.1016/j.jsr.2026.05.017 | 核实已发表，校正题目并补 DOI；98, 40–54 |
| 8 | 10.1016/j.physa.2025.130519 | 核对题目、作者，补卷号与文章号 |
| 9 | 10.1016/j.chaos.2025.117161 | 作者顺序改为 Hu、Gao、Wang、Lee |
| 10 | 10.1016/j.aei.2026.104790 | 题目改为正式的 “A prediction error-based method”；校正顺序并补 Abdel-Aty、DOI |
| 11 | 10.1016/j.ress.2026.112505 | 作者顺序改为 Hu、Wang、Lee；补卷号与文章号 |
| 12 | 10.1016/j.trc.2026.105712 | 将错误 DOI 尾号 102007 改为 105712 |
| 13 | 10.1016/j.scs.2026.107204 | 补 DOI、卷号与文章号；保留并核实 Hu 通讯作者标记 |
| 14 | 10.1016/j.trc.2025.105341 | 核对作者、题目与卷号；增加作者公开 PDF 中的方法框架原图 |
| 15 | 10.1016/j.apenergy.2026.129177 | 新增；427, Part F, 129177；明确 2026 在线与 2027 年 1 月卷期 |
| 16 | 10.1016/j.ress.2026.113793 | 新增 BRACE；2026-11-07 在线，Journal Pre-proof；不编造卷期 |

科学表述：将详情统一为“研究概述”，依据公开摘要介绍研究内容，避免将合作论文的全部工作归于个人。对 Granger 关联、跟驰残差解释及 BRACE 模型响应保留证据边界；充电论文说明历史回放与权衡，不将关联或预测筛选表述为已证明的政策因果收益。没有改动研究数据、重新估计结果或补造实验。

### 图示来源

- 原有 10 张研究图示保留，说明为原网站提供的资产；本轮未声称全部与出版版图号逐一对应。
- ID 14 使用[作者公开 PDF](https://sunderlandaj-1130.github.io/files/hu2025trc.pdf) 第 4 页的 Fig. 2，直接提取原嵌入图片，未修改内容。
- ID 5、6、7、15、16 在公开页面未取得论文原图。根据用户授权及已核验摘要绘制中英文 SVG 流程图；缩略图、图内与图注均区分“研究示意图”，附 DOI 来源，不冒充原论文图件，不包含模拟的实验曲线或数据。
- 机场论文摘要另核对[作者机构库](https://iris.polito.it/handle/11583/3015327)；Traffic Injury Prevention 论文另核对 [PubMed](https://pubmed.ncbi.nlm.nih.gov/41223339/)；Journal of Safety Research 论文另核对[出版页面](https://www.sciencedirect.com/science/article/abs/pii/S0022437526000927)。

核验完成：双语元数据一致、16 篇论文均有可加载图示与 DOI；本地资源、内部锚点、更新日期、脚本语法和 Git diff 空白检查通过。浏览器检查覆盖桌面、390px 与 320px 手机宽度、方向筛选、2027 年份、空结果、完整引用复制、图示弹窗、双语状态保留和深色主题；新增 SVG 文字未超出图框。

第三轮修订（2026-11-12）：在中英文简介及硕士经历中，将 Jaeyoung Jay Lee 链接至网站所有者指定的 Google Scholar 页面（用户 ID：XH0jqsUAAAAJ）。论文标题现在可直接打开对应 DOI；扩展桌面内容宽度，平板论文标题保持 18px，并优化短屏电脑上的侧栏滚动与联系入口可见性。既有 16 篇论文的元数据、图示及荣誉保持不变。

发布范围：网站所有者已授权将本轮改版发布至原仓库及 GitHub Pages 网址。凭证不保存在本仓库或交付包内。

## 头像

最终头像：frontend/profile-anime.png。使用网站所有者新上传的毕业照，调用内置 image_gen 工具进行动漫风格转换；原照片未被覆盖。

生成提示词：

> Use case: style-transfer. Asset type: final professional academic homepage portrait. Image 1 is the ONLY identity reference and edit target, a newly supplied graduation photograph. Transform this exact person and scene into a refined contemporary anime illustration with clean expressive linework, subtle cel shading and a softly painted background. Preserve his recognizable face, thin silver glasses, straight black hair with center-parted fringe, warm smile, adult age and natural proportions. Preserve the navy/purple graduation gown with bright yellow trim over a white shirt and the bouquet of blue, white and pale green flowers wrapped in pale blue paper. Soft sunlit leafy green campus background, simplified and muted so the face remains the focus. Portrait 4:5 composition from head to waist, full top of hair inside frame, bouquet and hands visible, with modest breathing room around head. Professional, friendly and scholarly, restrained anime eyes and facial proportions. Keep the small card reading '毕业快乐' if visible; omit other tiny illegible lettering, decorative stickers and logos. No added text, no watermarks, no extra people. Do not use any previous portrait or casual clothes.


