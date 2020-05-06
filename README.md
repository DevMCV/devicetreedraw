# devicetreedraw
Linux Device Tree to tree-like format (Ascii text image)

## Usage Example)
    cd linux-master/arch/arm64/boot/dts/qcom/
    python DeviceTreeDraw.py msm8996-mtp.dts

## Output)
    msm8996-mtp.dts
    `-- msm8996-mtp.dtsi
    `-- msm8996.dtsi
        |-- <dt-bindings/interrupt-controller/arm-gic.h>
        |-- <dt-bindings/clock/qcom,gcc-msm8996.h>
        |-- <dt-bindings/clock/qcom,mmcc-msm8996.h>
        |-- <dt-bindings/clock/qcom,rpmcc.h>
        |-- <dt-bindings/soc/qcom,apr.h>
        `-- msm8996-pins.dtsi
