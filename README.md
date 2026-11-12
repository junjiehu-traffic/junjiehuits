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
- 双语界面文字、研究概述、新增荣誉和动态：scripts/build.py 的 UI 字典。
- 样式：frontend/css/style.css；交互：frontend/js/main.js。
- 修改内容后运行 python scripts/build.py，同时重新生成两种语言的静态 HTML。
- 保留 frontend 路径，以兼容现有公开 URL。发布时将完整文件树提交至原仓库 main 分支，继续使用其现有 GitHub Pages 配置。

## 本次改版

- 参考 [Anleeno Academic](https://github.com/Anleeno/anleeno-academic) 的双栏结构、淡紫色调、论文图文条目和时间线，使用独立静态实现；未复用参考作者的照片、身份信息、论文或品牌素材。
- 中英文同步新增：2026 年 10 月入选中国科协青年科技人才培育工程博士生专项计划。入选事实与月份来自网站所有者本次提供的信息；计划说明链接指向中国科协官方管理办法，不代表该页面是个人入选公示。
- 更新日期为 2026-11-12。
- 论文按年份倒序展示；支持方向/年份/关键词联合筛选、研究概览、原始图示、引用复制、筛选状态随语言切换保留。
- 支持明暗主题、移动端导航、键盘焦点、Escape 关闭弹窗、减少动画偏好、打印布局。
- 页面正文直接写入 HTML；JavaScript 不可用时论文及贡献仍可阅读。
- 既有 PDF 简历 JunjieHu_CV.pdf 保留原文件；本次新增荣誉更新在网页中。

## 内容与核验记录

原站源码基线：5bdc18b025fa60e5afb0f194eea5143ee8e34de1。
以原站为内容依据，保留全部 14 篇论文的作者、年份、题目、期刊、贡献说明、原有外链和 10 张研究图示，以及教育经历和既有荣誉。本次没有改写论文的科学结论，也没有补造 DOI、摘要、引用数或收录等级。

核验完成：两语言论文元数据一致；与改版前逐条比对上述内容；本地图片、PDF、内部锚点存在；脚本语法与 Git diff 空白检查通过。浏览器检查覆盖桌面、手机、筛选、空结果、引用复制、图示弹窗、双语切换和深色主题。论文外部链接沿用原站，未逐篇重新核验出版社元数据。

## 头像

最终头像：frontend/profile-anime.png。使用网站所有者新上传的毕业照，调用内置 image_gen 工具进行动漫风格转换；原照片未被覆盖。

生成提示词：

> Use case: style-transfer. Asset type: final professional academic homepage portrait. Image 1 is the ONLY identity reference and edit target, a newly supplied graduation photograph. Transform this exact person and scene into a refined contemporary anime illustration with clean expressive linework, subtle cel shading and a softly painted background. Preserve his recognizable face, thin silver glasses, straight black hair with center-parted fringe, warm smile, adult age and natural proportions. Preserve the navy/purple graduation gown with bright yellow trim over a white shirt and the bouquet of blue, white and pale green flowers wrapped in pale blue paper. Soft sunlit leafy green campus background, simplified and muted so the face remains the focus. Portrait 4:5 composition from head to waist, full top of hair inside frame, bouquet and hands visible, with modest breathing room around head. Professional, friendly and scholarly, restrained anime eyes and facial proportions. Keep the small card reading '毕业快乐' if visible; omit other tiny illegible lettering, decorative stickers and logos. No added text, no watermarks, no extra people. Do not use any previous portrait or casual clothes.


