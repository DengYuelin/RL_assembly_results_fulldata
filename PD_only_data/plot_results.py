# -*- coding: utf-8 -*-
"""
# @Time    : 24/10/18 2:40 PM
# @Author  : ZHIMIN HOU
# @FileName: plot_result.py
# @Software: PyCharm
# @Github    ： https://github.com/hzm2016
"""

import matplotlib.pyplot as plt
import numpy as np
"""=================================Plot result====================================="""
YLABEL = ['Fx(N)', 'Fy(N)', 'Fz(N)', 'Mx(Nm)', 'My(Nm)', 'Mz(Nm)']
Title = ["X axis force", "Y axis force", "Z axis force",
         "X axis moment", "Y axis moment", "Z axis moment"]
COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink',
        'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise',
        'darkgreen', 'tan', 'salmon', 'gold', 'lightpurple', 'darkred', 'darkblue']
"""================================================================================="""

""" plot for chinese figure """
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False

FONT_SIZE = 34
LINEWIDTH = 4.

"""================================================================================="""
PREDICTION_LABELS = ['BE-DDPG', 'DDPG', 'VPB-DDPG', 'Dyna-DDPG', 'GPS']

DQN_LAVBELS = ['Typical DQN', 'VPB_DQN']
DDPG_LAVBELS = ['Typical DDPG', 'VPB_DDPG']


def plot_force(forces):
    plt.figure(figsize=(15, 10), dpi=300)
    # plt.title("Contact forces of one episode")
    new_forces = np.zeros((len(forces), 6), dtype=np.float32)
    for i in range(len(forces)):
        new_forces[i, :] = forces[i][0][:6]

    for j in range(6):
        plt.plot(new_forces[:, j], linewidth=3.)

    plt.xlabel("Steps", fontsize=30)
    plt.ylabel("Contact forces: F(N)/M(Nm)", fontsize=30)

    plt.legend(labels=['$F_x$', '$F_y$', '$F_z$', '$M_x$', '$M_y$', '$M_z$'], loc=2, bbox_to_anchor=(0.1, 1.15),
               borderaxespad=0., fontsize=30, ncol=3)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)

    plt.savefig('./figure/single_ddpg_forces_end.pdf')
    plt.show()


def plot_reward(result_path,
         x_labels="episodes", y_labels="reward", file_name='', render=True):
    """ Plot reward steps and times """

    plt.figure(figsize=(10, 8), dpi=300)
    plt.tight_layout(pad=3, w_pad=1., h_pad=0.5)
    plt.subplots_adjust(left=0.16, bottom=0.13, right=0.96, top=0.85, wspace=0.23, hspace=0.23)
    # plt.title('Search Result')
    result_data = np.load(result_path)
    mean_plot_data = np.mean(result_data, axis=0)
    print(mean_plot_data)
    std_plot_data = np.std(result_data, axis=0)
    print(std_plot_data)
    plt.plot(mean_plot_data, linewidth=3.75)
    plt.fill_between(np.arange(len(mean_plot_data)), mean_plot_data - std_plot_data,
                     mean_plot_data + std_plot_data, alpha=0.3)

    plt.ylabel(y_labels)
    plt.xlabel(x_labels)
    plt.xticks(fontsize=FONT_SIZE)
    plt.yticks(fontsize=FONT_SIZE)
    plt.xlabel("Episodes", fontsize=FONT_SIZE)
    plt.ylabel("Episode Reward", fontsize=FONT_SIZE)

    # plt.legend(YLABEL)
    plt.savefig(file_name)
    if render:
        plt.show()


def plot_comparision_curve(result_paths,
         file_name='./figure/comapre_different_options_reward.pdf', render=False):

    plt.figure(figsize=(10, 8), dpi=300)
    plt.tight_layout(pad=3, w_pad=1., h_pad=0.5)
    plt.subplots_adjust(left=0.16, bottom=0.13, right=0.96, top=0.85, wspace=0.23, hspace=0.23)

    # plt.title('Compare Single DDPG with Six Options', fontsize=30)

    for i in range(len(result_paths)):
        prediction_result = np.load(result_paths['path_' + str(i)])
        plt.plot(prediction_result, linewidth=LINEWIDTH)

    plt.legend(labels=PREDICTION_LABELS, loc=2, bbox_to_anchor=(-0.04, 1.20),
               borderaxespad=0., ncol=3, fontsize=24)
    # plt.legend(fontsize=30, labels=PREDICTION_LABELS)

    plt.xlabel("Episodes", fontsize=FONT_SIZE)
    plt.ylabel("Episode Reward", fontsize=FONT_SIZE)
    plt.xticks(fontsize=FONT_SIZE)
    plt.yticks(fontsize=FONT_SIZE)

    plt.savefig(file_name)

    if render:
        plt.show()


def plot_comparision_hist(result_paths, file_name='', render=False):

    plt.figure(figsize=(10, 8), dpi=300)
    plt.tight_layout(pad=3, w_pad=1., h_pad=0.5)
    plt.subplots_adjust(left=0.16, bottom=0.13, right=0.96, top=0.85, wspace=0.23, hspace=0.23)

    for i in range(len(result_paths)):
        result_data = np.load(result_paths['path_' + str(i)])
        plt.hist(result_data, bins=30, histtype="stepfilled")

    plt.legend(labels=PREDICTION_LABELS, loc=2, bbox_to_anchor=(-0.04, 1.20),
               borderaxespad=0., ncol=3, fontsize=24)

    plt.yticks(fontsize=FONT_SIZE)
    plt.xticks(np.arange(20., 45, 5), fontsize=FONT_SIZE)
    plt.ylabel('Frequency', fontsize=FONT_SIZE)
    plt.xlabel('Episode time(s)', fontsize=FONT_SIZE)
    plt.grid(axis="y")

    plt.savefig(file_name)

    if render:
        plt.show()


def plot_comparision_curve_with_variance(result_paths, file_name='', render=False):

    plt.figure(figsize=(10, 8), dpi=300)
    plt.tight_layout(pad=3, w_pad=1., h_pad=0.5)
    plt.subplots_adjust(left=0.16, bottom=0.13, right=0.98, top=0.98, wspace=0.23, hspace=0.23)

    for i in range(len(result_paths)):
        result_data = np.load(result_paths['path_' + str(i)])
        mean_plot_data = np.mean(result_data, axis=0)
        std_plot_data = np.mean(result_data, axis=0)

        plt.plot(mean_plot_data, linewidth=3.75)
        plt.fill_between(np.arange(len(mean_plot_data)), mean_plot_data - std_plot_data,
                         mean_plot_data + std_plot_data, alpha=0.3)

    plt.legend(fontsize=30, loc='best', labels=PREDICTION_LABELS)
    plt.xlabel("Episodes", fontsize=FONT_SIZE)
    plt.ylabel("Episode Reward", fontsize=FONT_SIZE)
    plt.xticks(fontsize=FONT_SIZE)
    plt.yticks(fontsize=FONT_SIZE)

    plt.savefig(file_name)

    if render:
        plt.show()


if __name__ == "__main__":

    # data = np.load("./pd/_epochs_50_episodes_50_rollout_steps_300states.npy")
    # print(data)
    plot_reward("./pd/_epochs_50_episodes_50_rollout_steps_300steps.npy",
         file_name="./pd/Double_norand_steps.pdf")