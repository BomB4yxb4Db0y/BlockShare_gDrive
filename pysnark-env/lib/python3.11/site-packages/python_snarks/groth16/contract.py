


def export_solidity_verifier(setup, output_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = dir_path + "/template/groth16_verifier.sol"

    with open(template_path, "r") as f:
        data = f.read()

        vkalpha1_str = str(setup["vk_verifier"]["vk_alpha_1"][0]) + "," + str(setup["vk_verifier"]["vk_alpha_1"][1])
        data = data.replace("<%vk_alpha1%>", vkalpha1_str)


        vkbeta2_str = "[" + str(setup["vk_verifier"]["vk_beta_2"][0][1]) + ", " +
            str(setup["vk_verifier"]["vk_beta_2"][0][0]) + "], [" +
            str(setup["vk_verifier"]["vk_beta_2"][1][1]) + ", " +
            str(setup["vk_verifier"]["vk_beta_2"][1][0]) + "]"
        data = data.replace("<%vk_beta2%>", vkbeta2_str)

        vkgamma2_str = "[" + str(setup["vk_verifier"]["vk_gamma_2"][0][1]) + ", " +
            str(setup["vk_verifier"]["vk_gamma_2"][0][0]) + "], [" +
            str(setup["vk_verifier"]["vk_gamma_2"][1][1]) + ", " +
            str(setup["vk_verifier"]["vk_gamma_2"][1][0]) + "]"
        data = data.replace("<%vk_gamma2%>", vkgamma2_str)

        vkdelta2_str = "[" + str(setup["vk_verifier"]["vk_delta_2"][0][1]) + ", " + 
            str(setup["vk_verifier"]["vk_delta_2"][0][0]) + "], [" + 
            str(setup["vk_verifier"]["vk_delta_2"][1][1]) + ", " + 
            str(setup["vk_verifier"]["vk_delta_2"][1][0]) + "]"
        data = data.replace("<%vk_delta2%>", vkdelta2_str)

        data = data.replace("<%vk_input_length%>", str(len(setup["vk_verifier"]["IC"]) - 1))
        data = data.replace("<%vk_ic_length%>", str(len(setup["vk_verifier"]["IC"])))

        vi = ""
        for i in range(len(setup["vk_verifier"]["IC"])):
            if vi != "":
                vi = vi + "        "
            vi = vi + f'vk.IC[{i}] = Pairing.G1Point({str(setup["vk_verifier"]["IC"][i][0])},' +
                f'{str(setup["vk_verifier"]["IC"][{i}][1])});\n'
        data = data.replace("<%vk_ic_pts%>", vi)

        with open(output_path, "w") as output:
            output.write(data)