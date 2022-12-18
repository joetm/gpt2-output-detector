GPT2 Output Detector
===

Not recommended for detecting ChatGPT output.

Usage
---

python3 gpt2-output-detector.py

Add your own text to gpt-detect-inputs.txt.
Evaluation takes place in pairs of text.
Add human-written text in uneven lines, followed by AI-written text.

Output
---

    Text            p_Human                 p_AI
    --------------  ----------------------  -------------------
    Section1_Human  0.00018413520592730492  0.9998158812522888
    Section1_AI     0.03656712919473648     0.9634328484535217
    ---             ---                     ---
    Section2_Human  0.8894263505935669      0.11057362705469131
    Section2_AI     0.5315855145454407      0.4684145152568817
    ---             ---                     ---
    Section3_Human  0.000267964496742934    0.9997320771217346
    Section3_AI     0.00017033822950907052  0.9998296499252319
    ---             ---                     ---
    Section4_Human  0.00019494970911182463  0.9998050332069397
    Section4_AI     0.00521185714751482     0.9947881698608398
    ---             ---                     ---
    Section5_Human  0.03990468010306358     0.9600952863693237
    Section5_AI     0.00016930530546233058  0.9998307228088379
    ---             ---                     ---
    ...
