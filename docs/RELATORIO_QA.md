# Relatório de QA

## Fontes e ambiente

`python scripts/validar_fontes.py` retornou OK: 20 slides, notas, GIFs, roteiros e briefs. A apresentação original permanece como referência. O exame das fontes não certifica os vídeos.

## Método

A verificação independente utiliza `python scripts/qa_videos.py`: presença, H.264, resolução, taxa de quadros e duração via ffprobe; geração de quadro médio em `output/qa/quadros/`. O arquivo `output/qa/verificacao_tecnica.json` registra os valores. A extração de quadros não substitui revisão humana visual e factual; vídeos não inspecionados permanecem pendentes. A meta de duração individual é aproximadamente 40–60 s.

## Revisão preliminar do código

- Cena 03: apresenta segmentação em partes de palavra e identifica explicitamente IDs e divisão como fictícios, variáveis por tokenizador. Falta examinar o vídeo renderizado.
- Cena 17: duas pesquisas independentes precedem verificação e integração; a legenda afirma que a revisão espera os dois resultados. Falta examinar o vídeo renderizado.
- As cenas que usam `FluxoBiblioteca` representam etapas com cartões e setas. Isso apresenta uma sequência textual, mas não demonstra necessariamente o mecanismo técnico exigido: atenção Q/K/V, KV Cache e demais conceitos exigem avaliação visual específica. Não considerá-las aprovadas apenas pela renderização.

## Pendências

Revisão visual de quadros e movimento de todas as cenas, alinhamento das legendas à narração, verificação das durações, precisão didática por cena, encadeamento final e teste do PowerPoint em aplicativo desktop. Atualizar este relatório após a geração dos vídeos. Ausência de áudio gerado ou de vídeo deve ser registrada como limitação, não como aprovação.

## Revisão independente das prévias 03 e 17

Foram inspecionados quadros em 12, 27 e 43 segundos das prévias de 480p15, em `/tmp/llm-previews/videos/prototipos/480p15/` (não são entregáveis finais). Cena 17: fluxo legível, ramos paralelos e dependência da verificação representados. Cena 03: divisão e IDs são identificados como fictícios, porém a seta e a caixa MODELO cruzam e cobrem a ressalva no terço inferior; correção solicitada antes da renderização final. Esta inspeção por amostragem não substitui QA dos MP4s Full HD nem revisão de movimento integral.

A prévia corrigida da cena 03 foi reinspecionada aos 35 s: a ressalva está legível e a colisão foi eliminada. A aprovação se limita a esse ponto visual e à precisão do exemplo mostrado.

## Full HD: primeira amostra

- Cena 03: `ffprobe` confirmou H.264, 1920×1080, 30 fps, 47 s; arquivo sem faixa de áudio no momento da inspeção. O quadro central extraído está legível e sem a colisão anterior. Como o roteiro de áudio/legenda provisório foi temporizado para 50 s, há diferença de 3 s a resolver na montagem, evitando truncar voz e legendas.
- Cenas 05 e 08: prévias 480p examinadas em 12, 27 e 43 s. A cena 05 apresenta colisão entre uma seta e o peso 0,10, solicitada correção. A cena 08 mostra Top-P 0,75 conservando os dois primeiros itens da distribuição ilustrativa, e não apresentou colisões nos quadros amostrados. Os percentuais exibidos são da distribuição original antes de renormalização.
- Cena 17: `ffprobe` confirmou H.264, 1920×1080, 30 fps, 51 s; arquivo sem áudio no momento da inspeção. O quadro central é legível e o diagrama mostra duas pesquisas e a revisão dependente das duas. A faixa de áudio e SRT precisam acompanhar a duração efetiva.

## Resultado desta execução

Foram gerados 20 MP4s mudos em `output/scenes/`, 20 cópias com narração em `output/scenes_narradas/` e o filme narrado. A execução final de `python scripts/qa_videos.py` registrou 21/21 arquivos H.264 de 1920×1080 válidos; as 20 cenas têm 30 fps e duração entre 46 e 51 segundos. As cópias narradas foram verificadas individualmente quanto à presença de áudio; o filme tem H.264, AAC, 30 fps e 961,815 s. A validação das fontes continua passando. Verificou-se que slides, roteiros e assets originais não foram alterados.

A narração pt-BR foi sintetizada localmente com eSpeak NG; os trechos e os tempos do SRT foram recalculados com as durações medidas. As legendas usam início e fim dos trechos sintetizados, não alinhamento por palavra; sincronismo fino com os movimentos, pronúncia e naturalidade da voz requerem escuta integral. O filme tem cortes diretos e não inclui transições elaboradas. Não foi testado PowerPoint desktop nem produzida uma cópia com vídeo incorporado. Manim MCP não estava disponível; Manim Community 0.22.1 foi instalado localmente. Nenhuma API paga foi usada; custo estimado de licenças e chamadas de API: zero, sem estimativa de custo de infraestrutura.

Os quadros centrais das 20 cenas foram examinados em `output/qa/contato.jpg`. Também houve revisão independente das prévias 03, 05, 08 e 17; as sobreposições das cenas 03, 05 e 17 foram corrigidas. Na cena 07, a sobreposição do percentual com o título foi corrigida e reinspecionada aos 38 s. Quadros centrais são amostras: não comprovam legibilidade durante toda a animação nem equivalem a revisão integral. A anotação automática `revisao_visual: pendente` no JSON se refere à aprovação integral, não à ausência de amostragem.

| Cenas | Resultado da amostra e pendências |
|---|---|
| 01–02 | Fluxos legíveis; a relação com a biblioteca é apresentada por rótulos e personagem, mas falta uma ambientação visual mais rica. |
| 03 | Divisão e IDs explicitamente fictícios; colisão corrigida. Rever sincronismo com a fala. |
| 04 | Diagrama de direção e cosseno; conferir contraste das legendas claras em tela pequena. |
| 05 | Fluxo Q/K/V e pesos; colisão corrigida. A soma ponderada precisa de representação mais explícita de todos os valores. |
| 06 | Etapas em cartões; não demonstra visualmente a operação interna das camadas com o detalhe solicitado. |
| 07–08 | Gráfico de probabilidades e seleção ilustrativa; 07 teve sobreposição corrigida. Validar toda a animação e o ritmo com a voz. |
| 09–16 | Fluxos legíveis em amostra, mas são diagramas sequenciais simplificados; precisam de animações específicas de mecanismo e de revisão factual e visual integral antes de aprovação. |
| 17 | Paralelismo e dependência mostrados; prévia e quadro central Full HD revisados. |
| 18–19 | Fluxos simplificados; faltam representações mais concretas de recuperação de memória e correção de erro. |
| 20 | Fronteira de confiança, acesso limitado, aprovação e auditoria aparecem progressivamente; revisar posicionamento do rótulo próximo ao cabeçalho e ampliar a demonstração visual. |

Portanto os vídeos constituem uma **versão de trabalho**, não uma entrega aprovada contra todos os critérios: o requisito de movimento explicativo específico para cada cena e o QA integral ainda não foram satisfeitos. Não foi realizada revisão auditiva integral nem validação de acessibilidade em dispositivo móvel.

## Alternativa de narração neural

Foi criada uma segunda versão do filme usando Piper 1.8.0 e voz pt_BR-faber-medium, sem API paga. A voz é sintetizada por frases inteiras, com ritmo e pausas moderados. O `ffprobe` confirmou H.264 1920×1080 a 30 fps, áudio AAC e duração de 961,815 s. Os 20 áudios couberam nas cenas originais; as 186 legendas têm tempos válidos e ordenados. A marcação dentro de cada frase é proporcional, não alinhamento fonético; pronúncia, naturalidade, sincronismo com imagens e qualidade para ouvintes precisam de revisão auditiva humana. A versão anterior foi preservada.

## Voz Google e glossário técnico

Uma nova versão usa voz pt-BR fornecida pelo Google Translate via gTTS, que envia o texto do roteiro a um serviço externo. Cada cena foi ajustada à duração de sua narração e contém uma faixa que relaciona termos técnicos a elementos da biblioteca; o glossário completo também está em `output/glossario/`. A narração da cena 07 foi corrigida para citar Brasília, de acordo com a imagem.

A validação com ffprobe confirmou 20 cenas H.264, 1920×1080, 30 fps e áudio AAC; as pausas calculadas entre o fim da última frase e o fim de cada cena ficaram entre 1,107 e 1,120 segundo. O filme tem 1.005,835 segundos e áudio AAC; as 186 legendas têm tempos ordenados. Foram inspecionados quadros centrais das 20 cenas e amostras adicionais das cenas 01, 05 e 20; os resultados estão em `output/qa/contato_google.jpg` e `output/qa/verificacao_google.json`. A cena 20 dura cerca de 62 segundos devido ao conteúdo narrado. A narração não foi ouvida integralmente, e a sincronização dos trechos de legenda dentro das frases é aproximada; pode haver sobreposição da legenda externa com a faixa do glossário dependendo do reprodutor. As limitações didáticas e de animação da versão de trabalho continuam aplicáveis.

## Piper com cenas retimadas

O filme `IA_Biblioteca_Piper_Sincronizado.mp4` foi montado com voz Piper pt-BR e as faixas do glossário. As 20 cenas foram verificadas com ffprobe: H.264, 1920×1080, 30 fps e AAC. A pausa calculada entre o término do último trecho sintetizado e o fim da cena ficou entre 1,086 e 1,100 segundo; o filme tem 637,926 segundos. As 186 legendas apresentam tempos válidos e ordenados. A imagem da primeira cena foi examinada como amostra. O roteiro usa a correção da cena 07 para Brasília. As animações foram aceleradas proporcionalmente à duração de cada cena; isso não garante correspondência exata entre cada fala e cada elemento visual. Não foi feita escuta integral ou revisão visual de todos os quadros.

## Pronúncia inglesa com Piper

O roteiro foi percorrido com um dicionário de 33 entradas IPA: 48 ocorrências de termos e siglas em inglês foram convertidas para fonemas na entrada do sintetizador, mantendo a escrita original nas legendas. Confirmou-se que todos os símbolos constam do mapa do modelo. A checagem não comprova a qualidade auditiva nem sotaque nativo; a voz Piper foi treinada em português e precisa de escuta humana, especialmente de embedding, query, key, value e siglas. Não houve escuta integral nesta execução.

Os 20 MP4s têm H.264 1920×1080 a 30 fps e áudio AAC; pausas finais medidas entre 1,085 e 1,100 s. As 186 legendas têm tempos ordenados; sua temporização intra-frase é aproximada. O filme dura 636,490 s. A cena 05 foi disponibilizada como amostra para avaliação auditiva. As limitações de sincronização visual proporcional e de revisão integral anteriores permanecem.
