import numpy as np

from ConfigPlot import ConfigPlot_EigenMode_DiffMass, ConfigPlot_YFixed_rec, ConfigPlot_DiffMass_SP
from MD_functions_2 import MD_VibrSP_ConstV_Yfixed_DiffK, FIRE_YFixed_ConstV_DiffK, MD_VibrSP_ConstV_Yfixed_DiffK2
from DynamicalMatrix import DM_mass_DiffK_Yfixed
from plot_functions import Line_single, Line_multi
from ConfigPlot import ConfigPlot_DiffStiffness3, ConfigPlot_DiffStiffness4
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

class switch():
    def evaluate(stiffness, ind1, ind2, noise):       
        #%% Initial Configuration
        #k1 = 1.
        #k2 = 10.
        
        n_col = 6
        n_row = 5
        N = n_col*n_row
        
        Nt_fire = 1e6
        
        dt_ratio = 40
        Nt_SD = 1e5
        Nt_MD = 1e5
        
        
        dphi_index = -1
        dphi = 10**dphi_index
        d0 = 0.1
        d_ratio = 1.1
        Lx = d0*n_col
        Ly = (n_row-1)*np.sqrt(3)/2*d0+d0
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        
        phi0 = N*np.pi*d0**2/4/(Lx*Ly)
        d_ini = d0*np.sqrt(1+dphi/phi0)
        D = np.zeros(N)+d_ini
        #D = np.zeros(N)+d0 
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        for i_row in range(1, n_row+1):
            for i_col in range(1, n_col+1):
                ind = (i_row-1)*n_col+i_col-1
                if i_row%2 == 1:
                    x0[ind] = (i_col-1)*d0
                else:
                    x0[ind] = (i_col-1)*d0+0.5*d0
                y0[ind] = (i_row-1)*np.sqrt(3)/2*d0
        y0 = y0+0.5*d0
        
        mass = np.zeros(N) + 1
        #k_list = np.array([k1, k2, k1 * k2 / (k1 + k2)])
        #k_type = indices
        
        # Steepest Descent to get energy minimum      
        x_ini, y_ini, p_now = FIRE_YFixed_ConstV_DiffK(Nt_fire, N, x0, y0, D, mass, Lx, Ly, stiffness)


        # specify the input ports and the output port
        ind_in1 = ind1 #int((n_col+1)/2) - 1 + n_col * 2
        ind_in2 = ind2 #ind_in1 + 2
        ind_out = int(N-int((n_col+1)/2))
        ind_s = int((n_col+1)/2)
        #ind_fix = int((n_row+1)/2)*n_col-int((n_col+1)/2)


        B = 1
        Nt = 1e4 # it was 1e5 before, i reduced it to run faster

        # we are designing a nand gate at this amplitude and this freq
        Amp_Vibr = 1e-3
        Freq_Vibr = 10

        # case 00: output: 1
        Amp_Vibr1 = 0 * Amp_Vibr
        Amp_Vibr2 = 0 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain00 = out1/(src+inp1+inp2)

        # case 01: output: 1
        Amp_Vibr1 = 0 * Amp_Vibr
        Amp_Vibr2 = 1 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain01 = out1/((src+inp1+inp2))

        # case 10: output: 1
        Amp_Vibr1 = 1 * Amp_Vibr
        Amp_Vibr2 = 0 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain10 = out1/((src+inp1+inp2))

        # case 11: output: 0
        Amp_Vibr1 = 1 * Amp_Vibr
        Amp_Vibr2 = 1 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain11 = out1/((src+inp1+inp2))

        nandness = (abs(1-round(gain00, 2)) + abs(1-round(gain01, 2)) + abs(1-round(gain10, 2)) + abs(0-round(gain11, 2)))/4

        worst = max(abs(1-round(gain00, 2)), abs(1-round(gain01, 2)), abs(1-round(gain10, 2)), abs(0-round(gain11, 2)))

        return [-1 * worst, gain00, gain01, gain10, gain11]

    def showPacking(stiffness, ind1, ind2):
        #k1 = 1.
        #k2 = 10.

        n_col = 6
        n_row = 5
        N = n_col*n_row

        m1=1
        m2=10
        
        dphi_index = -1
        dphi = 10**dphi_index
        d0 = 0.1
        Lx = d0*n_col
        Ly = (n_row-1)*np.sqrt(3)/2*d0+d0
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        
        phi0 = N*np.pi*d0**2/4/(Lx*Ly)
        d_ini = d0*np.sqrt(1+dphi/phi0)
        D = np.zeros(N)+d_ini
        #D = np.zeros(N)+d0 
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        for i_row in range(1, n_row+1):
            for i_col in range(1, n_col+1):
                ind = (i_row-1)*n_col+i_col-1
                if i_row%2 == 1:
                    x0[ind] = (i_col-1)*d0
                else:
                    x0[ind] = (i_col-1)*d0+0.5*d0
                y0[ind] = (i_row-1)*np.sqrt(3)/2*d0
        y0 = y0+0.5*d0
        
        mass = np.zeros(N) + 1
        #k_list = np.array([k1, k2, k1 * k2 / (k1 + k2)])
        #k_type = indices

        # specify the input ports and the output port
        ind_in1 = ind1 #int((n_col+1)/2) - 1 + n_col * 2
        ind_in2 = ind2 #ind_in1 + 2
        ind_out = int(N-int((n_col+1)/2))
        ind_s = int((n_col+1)/2)
        #ind_fix = int((n_row+1)/2)*n_col-int((n_col+1)/2)

        # show packing
        ConfigPlot_DiffStiffness4(N, x0, y0, D, [Lx,Ly], stiffness, 0, '/Users/atoosa/Desktop/results/packing.pdf', ind_in1, ind_in2, ind_s, ind_out)


    def plotInOut(stiffness, ind1, ind2, noise):

        #%% Initial Configuration
        #k1 = 1.
        #k2 = 10. 
        m1 = 1
        m2 = 10
        
        n_col = 6
        n_row = 5
        N = n_col*n_row
        
        Nt_fire = 1e6
        
        dt_ratio = 40
        Nt_SD = 1e5
        Nt_MD = 1e5
        
        
        dphi_index = -1
        dphi = 10**dphi_index
        d0 = 0.1
        d_ratio = 1.1
        Lx = d0*n_col
        Ly = (n_row-1)*np.sqrt(3)/2*d0+d0
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        
        phi0 = N*np.pi*d0**2/4/(Lx*Ly)
        d_ini = d0*np.sqrt(1+dphi/phi0)
        D = np.zeros(N)+d_ini
        #D = np.zeros(N)+d0 
        
        x0 = np.zeros(N)
        y0 = np.zeros(N)
        for i_row in range(1, n_row+1):
            for i_col in range(1, n_col+1):
                ind = (i_row-1)*n_col+i_col-1
                if i_row%2 == 1:
                    x0[ind] = (i_col-1)*d0
                else:
                    x0[ind] = (i_col-1)*d0+0.5*d0
                y0[ind] = (i_row-1)*np.sqrt(3)/2*d0
        y0 = y0+0.5*d0
        
        mass = np.zeros(N) + 1
        #k_list = np.array([k1, k2, k1 * k2 / (k1 + k2)])
        #k_type = indices
        
        # Steepest Descent to get energy minimum      
        x_ini, y_ini, p_now = FIRE_YFixed_ConstV_DiffK(Nt_fire, N, x0, y0, D, mass, Lx, Ly, stiffness)

        # calculating the bandgap - no need to do this in this problem
        w, v = DM_mass_DiffK_Yfixed(N, x_ini, y_ini, D, mass, Lx, 0.0, Ly, stiffness)
        w = np.real(w)
        v = np.real(v)
        freq = np.sqrt(np.absolute(w))
        ind_sort = np.argsort(freq)
        freq = freq[ind_sort]
        v = v[:, ind_sort]
        ind = freq > 1e-4
        eigen_freq = freq[ind]
        eigen_mode = v[:, ind]
        w_delta = eigen_freq[1:] - eigen_freq[0:-1]
        index = np.argmax(w_delta)
        F_low_exp = eigen_freq[index]
        F_high_exp = eigen_freq[index+1]

        plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.scatter(np.arange(0, len(eigen_freq)), eigen_freq, marker='x', color='blue', s=200, linewidth=3)
        plt.xlabel(r"Index $(k)$", fontsize=32)
        plt.ylabel(r"Frequency $(\omega)$", fontsize=32)
        plt.title("Frequency Spectrum", fontsize=32, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        props = dict(facecolor='green', alpha=0.1)
        myText = r'$\omega_{low}=$'+"{:.2f}".format(F_low_exp)+"\n"+r'$\omega_{high}=$'+"{:.2f}".format(F_high_exp)+"\n"+r'$\Delta \omega=$'+"{:.2f}".format(max(w_delta))
        plt.text(0.78, 0.15, myText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=28, bbox=props)
        plt.xticks(fontsize=28)
        plt.yticks(fontsize=28)
        plt.tight_layout()
        plt.show()

        print("specs:")

        print(F_low_exp)
        print(F_high_exp)
        print(max(w_delta))

        # specify the input ports and the output port
        ind_in1 = ind1 #int((n_col+1)/2) - 1 + n_col * 2
        ind_in2 = ind2 #ind_in1 + 2
        ind_out = int(N-int((n_col+1)/2))
        ind_s = int((n_col+1)/2)
        #ind_fix = int((n_row+1)/2)*n_col-int((n_col+1)/2)

        B = 1
        Nt = 1e4 # it was 1e5 before, i reduced it to run faster

        # we are designing a nand gate at this amplitude and this freq
        Amp_Vibr = 1e-3
        Freq_Vibr = 10

        # case 00: output: 1
        Amp_Vibr1 = 0 * Amp_Vibr
        Amp_Vibr2 = 0 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain00 = out1/(src+inp1+inp2)

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(freq_fft, fft_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(freq_fft, fft_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(freq_fft, fft_x_out, color='red', label='Output', linestyle='solid', linewidth=2)
        plt.xlabel("Frequency", fontsize=28)
        plt.ylabel("Amplitude of FFT", fontsize=28)
        plt.title("input = 00", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        plt.legend(loc='upper right', fontsize=32)
        #plt.axvline(x=Freq_Vibr, color='purple', linestyle='solid', alpha=0.5)
        myText = 'Gain='+"{:.4f}".format(gain00)
        plt.text(0.5, 0.9, myText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=28)
        #plt.ylim((0, 0.0015))
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        plt.tight_layout()
        plt.show()

        x_in1, x_in2, x_s, x_out = MD_VibrSP_ConstV_Yfixed_DiffK2(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(x_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(x_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(x_out-np.mean(x_out[1000:]), color='red', label='Output', linestyle='solid', linewidth=3)
        plt.hlines(y=0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.hlines(y=-0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.xlabel("Time Steps", fontsize=28)
        plt.ylabel("Displacement", fontsize=28)
        plt.title("input = 00", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        plt.legend(loc='upper right', fontsize=32)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((-0.0025, 0.0025))
        plt.xlim((0, 5000))
        plt.tight_layout()
        plt.show()

        # case 01: output: 1
        Amp_Vibr1 = 0 * Amp_Vibr
        Amp_Vibr2 = 1 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain01 = out1/((src+inp1+inp2))

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(freq_fft, fft_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(freq_fft, fft_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(freq_fft, fft_x_out, color='red', label='Output', linestyle='solid', linewidth=2)
        plt.xlabel("Frequency", fontsize=28)
        plt.ylabel("Amplitude of FFT", fontsize=28)
        plt.title("input = 01", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        #plt.axvline(x=Freq_Vibr, color='purple', linestyle='solid', alpha=0.5)
        myText = 'Gain='+"{:.4f}".format(gain01)
        plt.text(0.5, 0.9, myText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=28)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((0, 0.0015))
        plt.tight_layout()
        plt.show()

        x_in1, x_in2, x_s, x_out = MD_VibrSP_ConstV_Yfixed_DiffK2(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(x_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(x_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(x_out-np.mean(x_out[1000:]), color='red', label='Output', linestyle='solid', linewidth=3)
        plt.hlines(y=0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.hlines(y=-0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.xlabel("Time Steps", fontsize=28)
        plt.ylabel("Displacement", fontsize=28)
        plt.title("input = 01", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((-0.0025, 0.0025))
        plt.xlim((0, 5000))
        plt.tight_layout()
        plt.show()

        # case 10: output: 1
        Amp_Vibr1 = 1 * Amp_Vibr
        Amp_Vibr2 = 0 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain10 = out1/((src+inp1+inp2))

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(freq_fft, fft_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(freq_fft, fft_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(freq_fft, fft_x_out, color='red', label='Output', linestyle='solid', linewidth=2)
        plt.xlabel("Frequency", fontsize=28)
        plt.ylabel("Amplitude of FFT", fontsize=28)
        plt.title("input = 10", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        #plt.axvline(x=Freq_Vibr, color='purple', linestyle='solid', alpha=0.5)
        myText = 'Gain='+"{:.4f}".format(gain10)
        plt.text(0.5, 0.9, myText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=28)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((0, 0.0015))
        plt.tight_layout()
        plt.show()

        x_in1, x_in2, x_s, x_out = MD_VibrSP_ConstV_Yfixed_DiffK2(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)
        
        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(x_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(x_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(x_out-np.mean(x_out[1000:]), color='red', label='Output', linestyle='solid', linewidth=3)
        plt.hlines(y=0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.hlines(y=-0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.xlabel("Time Steps", fontsize=28)
        plt.ylabel("Displacement", fontsize=28)
        plt.title("input = 10", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((-0.0025, 0.0025))
        plt.xlim((0, 5000))
        plt.tight_layout()
        plt.show()

        # case 11: output: 0
        Amp_Vibr1 = 1 * Amp_Vibr
        Amp_Vibr2 = 1 * Amp_Vibr
        
        # changed the resonator to one in MD_functions file and vibrations in x direction
        freq_fft, fft_in1, fft_in2, fft_s, fft_x_out, fft_y_out, mean_cont, nt_rec, Ek_now, Ep_now, cont_now = MD_VibrSP_ConstV_Yfixed_DiffK(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out1 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input1 at driving frequency
        inp1 = fft_in1[index_-1] + (fft_in1[index_]-fft_in1[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        ind = np.where(freq_fft>Freq_Vibr)
        index_=ind[0][0]
        # fft of the output port at the driving frequency
        out2 = fft_x_out[index_-1] + (fft_x_out[index_]-fft_x_out[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))
        # fft of input2 at driving frequency
        inp2 = fft_in2[index_-1] + (fft_in2[index_]-fft_in2[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        # fft of source at driving frequency
        src = fft_s[index_-1] + (fft_s[index_]-fft_s[index_-1])*((Freq_Vibr-freq_fft[index_-1])/(freq_fft[index_]-freq_fft[index_-1]))

        gain11 = out1/((src+inp1+inp2))

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(freq_fft, fft_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(freq_fft, fft_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(freq_fft, fft_x_out, color='red', label='Output', linestyle='solid', linewidth=2)
        plt.xlabel("Frequency", fontsize=28)
        plt.ylabel("Amplitude of FFT", fontsize=28)
        plt.title("input = 11", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        #plt.axvline(x=Freq_Vibr, color='purple', linestyle='solid', alpha=0.5)
        myText = 'Gain='+"{:.4f}".format(gain11)
        plt.text(0.5, 0.9, myText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=28)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((0, 0.0015))
        plt.tight_layout()
        plt.show()

        x_in1, x_in2, x_s, x_out = MD_VibrSP_ConstV_Yfixed_DiffK2(stiffness, B, Nt, N, x_ini, y_ini, D, mass, [Lx, Ly], Freq_Vibr, Amp_Vibr, ind_s, Amp_Vibr1, ind_in1, Amp_Vibr2, ind_in2, ind_out, noise)

        fig = plt.figure(figsize=(6.4,4.8))
        ax = plt.axes()
        plt.plot(x_in1, color='lightgreen', label='Input1', linestyle='solid', linewidth=5)
        plt.plot(x_in2, color='blue', label='Input2', linestyle='dashed', linewidth=1)
        plt.plot(x_out-np.mean(x_out[1000:], axis=0), color='red', label='Output', linestyle='solid', linewidth=3)
        plt.hlines(y=0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.hlines(y=-0.001, xmin=0, xmax=1e4, linewidth=2, linestyle='--', color='magenta', alpha=0.8)
        plt.xlabel("Time Steps", fontsize=28)
        plt.ylabel("Displacement", fontsize=28)
        plt.title("input = 11", fontsize=28, fontweight="bold")
        plt.grid(color='skyblue', linestyle=':', linewidth=0.75)
        #plt.legend(loc='upper right', fontsize=32)
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        #plt.ylim((-0.0025, 0.0025))
        plt.xlim((0, 5000))
        plt.tight_layout()
        plt.show()

        print("gain00:")
        print(gain00)
        print("gain01:")
        print(gain01)
        print("gain10:")
        print(gain10)
        print("gain11:")
        print(gain11)

        nandness = (abs(1-round(gain00, 2)) + abs(1-round(gain01, 2)) + abs(1-round(gain10, 2)) + abs(0-round(gain11, 2)))/4
        print("nandness: "+str(round(nandness, 3)))

        return [gain00, gain01, gain10, gain11]
