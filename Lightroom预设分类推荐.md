# Lightroom 预设分类推荐

## 先说结论

你下载的这批文件可以使用，但它们不是通常意义上的 LUT。

- 文件里没有 `.cube` LUT。
- 实际内容主要是 Lightroom Classic 使用的 `.xmp` 预设、Look 和 Profile。
- 你当前安装的是 **Lightroom Classic 15.6**，这批文件主要按 Camera Raw 11.0 和 15.4 生成，整体兼容。
- 这批 XMP 不适合直接用于 DaVinci Resolve、Premiere Pro 或视频调色。

## 文件情况

- 共 18 个 ZIP，其中两个 Atmos 压缩包完全相同，因此实际只有 **17 套不同预设**。
- 大多数压缩包只有一个主预设，“Color 100”“Instant 100”等是名称，不代表包内有一百个预设。
- 每个压缩包通常同时包含：
  - `2. Lightroom (.xmp)`：当前版本使用的新版预设。
  - `3. Lightroom (.lrtemplate)`：旧版 Lightroom 的预设，不需要导入。
- `Olive & Earth`、`Fast Film`、`Portra Colour`、`Moody Lake` 还额外带有 Look 或 Profile 版本。
- 注意不要同时导入同名普通预设和 Look，否则预设列表里可能出现重复名称。

## 分类推荐

### 1. 人像与肤色

| 预设 | 风格 | 适合照片 | 推荐度 |
|---|---|---|---|
| Portra Colour | 柯达 Portra 400 风格，肤色柔和，层次自然 | 自然光人像、婚礼、生活方式、城市人像 | 很高 |
| Portra 800 | 暖调、对比和饱和度更高，带颗粒感 | 弱光人像、夜景人像、色彩鲜明的生活照 | 很高 |
| KDK Colour | 偏 Kodachrome 的浓郁红黄色与胶片质感 | 街拍人像、纪实、旅行人物 | 高 |
| Sunscreen | 明亮、通透、暖调 | 海边、夏季、逆光人像 | 高 |
| Boho Chic | 低饱和、梦幻、柔和 | 卧室、咖啡馆、婚礼细节、柔和氛围人像 | 中 |

**优先选择：** 先把自然光人像做成偏清透自然的效果，用 `Portra Colour`；想增加情绪和胶片感时再用 `Portra 800`。

### 2. 风景与自然环境

| 预设 | 风格 | 适合照片 | 推荐度 |
|---|---|---|---|
| Olive & Earth | 暖色、低饱和绿色、柔和胶片感 | 森林、草地、旅行、自然光人像 | 很高 |
| Atmos | 厚重雾感、色彩明显、中调氛围强 | 清晨雾气、山地、湖泊 | 高 |
| Sun Waves | 蓝天与暖色高光并重，明亮鲜艳 | 海岸线、夏日、蓝天白云 | 高 |
| Beautiful Sunrise | 暖色到冷色的渐变增强 | 日出、日落、黄金时刻 | 中高 |

**优先选择：** `Olive & Earth` 最适合当前流行的低饱和胶片风；遇到雾天、阴天和山地，用 `Atmos`；海边和日落则用 `Sun Waves`。

### 3. 城市、街拍与电影感

| 预设 | 风格 | 适合照片 | 推荐度 |
|---|---|---|---|
| Kyoto | 红绿浓郁、细节清晰、色彩鲜明 | 城市旅行、日本街景、夜市 | 高 |
| Vintage City | 低饱和、柔焦、复古怀旧 | 老城区、建筑、城市漫步 | 高 |
| Moody Lake | 冷白平衡、低饱和、电影感 | 阴天、城市、情绪人像、湖泊 | 很高 |
| Slide Film | 高对比、高饱和、正片胶片感 | 强光街景、旅行、建筑 | 中高 |

**优先选择：** 想要冷调电影感，用 `Moody Lake`；想要浓郁城市色彩，用 `Kyoto`；想要安静复古的氛围，用 `Vintage City`。

### 4. 日常、旅行与社交媒体

| 预设 | 风格 | 适合照片 | 推荐度 |
|---|---|---|---|
| Fast Film | 暖调、柔和高光、轻微颗粒与光晕 | 旅行日记、咖啡馆、生活记录 | 很高 |
| Instant 100 | Fuji FP-100C 拍立得风格，暖调、褪色阴影 | 朋友合照、复古日常、旅行纪念 | 很高 |
| Color 100 | 暖调富士日常胶片感 | 日常快照、晴天街景、食物 | 高 |
| Insta Film | 对比更高、社交平台风格明显 | 社交媒体、穿搭、探店 | 中 |

**优先选择：** 记录日常时，`Fast Film` 和 `Instant 100` 最百搭；晴天和旅行可以用 `Color 100`。

## 第一轮导入建议

不要一次性把 17 套预设全部堆进面板。第一阶段只导入以下 7 个：

1. `Portra Colour`：人像基础预设。
2. `Portra 800`：更浓郁的弱光和人像效果。
3. `Olive & Earth`：自然、低饱和胶片风。
4. `Moody Lake`：冷调电影感。
5. `KDK Colour`：浓郁复古胶片。
6. `Fast Film`：日常旅行万能款。
7. `Color 100`：晴天和日常生活照片。

风景拍得多，再加入：

- `Atmos`
- `Sun Waves`
- `Beautiful Sunrise`

城市街拍拍得多，再加入：

- `Kyoto`
- `Vintage City`
- `Slide Film`

## 按拍摄场景快速选择

| 拍摄场景 | 首选 | 备选 |
|---|---|---|
| 自然光人像 | Portra Colour | Portra 800 |
| 弱光人像 | Portra 800 | KDK Colour |
| 森林、草地、绿植 | Olive & Earth | Atmos |
| 山区、阴天、雾气 | Atmos | Moody Lake |
| 海边、蓝天 | Sun Waves | Sunscreen |
| 日出、日落 | Beautiful Sunrise | Sun Waves |
| 城市街拍 | Kyoto | Vintage City |
| 情绪人像 | Moody Lake | KDK Colour |
| 咖啡馆、旅行日记 | Fast Film | Instant 100 |
| 社交媒体 | Fast Film | Insta Film |
| 复古纪念照 | Instant 100 | Vintage City |
| 强对比、高饱和 | Slide Film | Kyoto |

## 在 Lightroom Classic 中导入

1. 解压需要使用的 ZIP。
2. 进入 `2. Lightroom (.xmp)` 文件夹。
3. 只选择普通 `.xmp`，不要导入 `3. Lightroom (.lrtemplate)` 中的旧文件。
4. 在 Lightroom Classic 中选择：

   **文件 → 导入配置文件和预设**

5. 普通预设会出现在“预设”面板。
6. Look 或 Profile 会出现在“配置文件”区域，可以从配置文件浏览器中查找。

直接导入 ZIP 也可能成功，但先解压并挑选 XMP 更稳妥，也不容易误导入旧格式。

## 初学调色的使用顺序

1. 先修正曝光和白平衡，再套预设。
2. 先使用预设的普通 `.xmp` 版本。
3. 带强度控制的 Look 建议从中等强度开始，不要直接拉满。
4. 套用后检查肤色、天空和绿色，再微调曝光、高光、阴影、白平衡和 HSL。
5. 不要连续叠加多个预设；需要风格差异时复制虚拟副本进行比较。
6. 把预设当作调色起点，不要把一键效果当作最终成品。

## 整理建议

- `LightroomAtmosPresetpro.zip` 与 `LightroomAtmosPresetpro 2.zip` 完全重复，只保留一个。
- `颜色.png` 是 CMYK 色相环，与 Lightroom 预设无关。
- 套餐中的 PDF 是完整的预设目录和效果参考，可以保留。
- 旧 `.lrtemplate` 文件可以忽略；当前版本统一使用 `.xmp`。
