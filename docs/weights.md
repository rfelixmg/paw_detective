Cats and dogs `weights`
---

Please download the latest weights.

# Processed dataset
1. **To download and extract the processed dataset, run the following commands in your terminal:**

    ```bash
    mkdir weights
    cd weights/
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=144dVCpxYt2xWSpyjNKYtvgm4F2VRR1l2" -O best.pt && rm -rf /tmp/cookies.txt

    WEIGHTS=$PWD/
    ```

    Make sure to replace `WEIGHTS` with the appropriate directory path.
