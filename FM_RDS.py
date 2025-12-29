#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: student
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import rds
import satellites.components.demodulators
import sip
import threading



class FM_RDS(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "FM_RDS")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000

        ##################################################
        # Blocks
        ##################################################

        self.satellites_bpsk_demodulator_0 = satellites.components.demodulators.bpsk_demodulator(baudrate = 1187, samp_rate = samp_rate, f_offset = 0, differential = False, manchester = False, iq = False, options="")
        self.rds_encoder_0 = rds.encoder(0, 14, True, 'WDR 3', 89.8e6,
        			True, False, 13, 3,
        			147, 'GNU Radio <3')

        self.rds_decoder_0 = rds.decoder(True, True)
        self.rational_resampler_xxx_0_1_1 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=25,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=2000,
                decimation=441,
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_1 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Retereived [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_1_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0_1_1.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_1_1_win)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " Received [53,54,69]  ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_1_0_0_win)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " L [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0_1_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_1_0_win)
        self.qtgui_waterfall_sink_x_0_1_0_0_1 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "R [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0_1.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0_1.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_1_win)
        self.qtgui_waterfall_sink_x_0_1_0_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " Transmitted [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_0_win)
        self.qtgui_waterfall_sink_x_0_1_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "DSB SC [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_win)
        self.qtgui_waterfall_sink_x_0_1_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " L-R [53,54,69]  ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_0_win)
        self.qtgui_waterfall_sink_x_0_0_1 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "R [53,54,69]  ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_1.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_0_1.set_plot_pos_half(not True)

        labels = ['L', 'R', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_1.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_1_win)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_RECTANGULAR, #wintype
            0, #fc
            samp_rate, #bw
            " L+R [53,54,69]  ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "L [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['L', 'R', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " Original [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            " Retereived [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Transmitted [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Original [53,54,69] ", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_1_0_0_1_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Reterieved [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_1_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_1_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_1_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_1_1_win)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Received [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_1_0_0_win)
        self.qtgui_freq_sink_x_0_1_0_0_1_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "L [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_1_0_win)
        self.qtgui_freq_sink_x_0_1_0_0_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "R [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_1_win)
        self.qtgui_freq_sink_x_0_1_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " Transmitted [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_0_win)
        self.qtgui_freq_sink_x_0_1_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " DSB SC [53,54,69] ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_win)
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " L-R  [53,54,69]  ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " L+R ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Stereo [53,54,69] ", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['L', 'R', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["dark blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            " Original [53,54,69]  ", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                8000,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                14000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                14000,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                7500,
                1500,
                window.WIN_HAMMING,
                6.76))
        self.digital_psk_mod_0 = digital.psk.psk_mod(
            constellation_points=4,
            mod_code="gray",
            differential=False,
            samples_per_symbol=4,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\Asus\\Downloads\\Thalapathy_Kacheri_-_Anirudh_Ravichander.mp3', True)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_ff(0.1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(0.1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.5)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_3_0 = blocks.add_vff(1)
        self.blocks_add_xx_3 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_3_1_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                55000,
                59000,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                37500,
                38500,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                11000,
                14000,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                24000,
                52000,
                3000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                10500,
                13500,
                1500,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0_0_0_0_1 = audio.sink(48000, '', True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=(samp_rate*5),
        	tau=(75e-6),
        	max_dev=75e3,
        	fh=(-1),
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=(samp_rate*5),
        	audio_decimation=5,
        )
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 66000, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 19000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 38000, 5, 0, 0)
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=samp_rate, tau=(75e-6), fh=(-1.0))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_preemph_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_3_1_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.analog_wfm_rcv_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_1_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0, 0))
        self.connect((self.analog_wfm_tx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0_0_1, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_3_0, 0), (self.blocks_add_xx_3_0, 1))
        self.connect((self.band_pass_filter_3_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_1, 0))
        self.connect((self.band_pass_filter_3_0, 0), (self.qtgui_waterfall_sink_x_0_1_0_0_1, 0))
        self.connect((self.band_pass_filter_3_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_3_1_0, 0), (self.satellites_bpsk_demodulator_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0_1_0_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_waterfall_sink_x_0_1_0_0_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.low_pass_filter_2, 0))
        self.connect((self.blocks_add_xx_3_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_1_1, 0))
        self.connect((self.blocks_add_xx_3_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_3_0, 0), (self.qtgui_waterfall_sink_x_0_1_0_0_1_1, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.rds_decoder_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_1, 3))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_1_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.band_pass_filter_3_1, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1_0, 0))
        self.connect((self.blocks_sub_xx_1, 0), (self.band_pass_filter_3_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_xx_3, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_sub_xx_1, 0))
        self.connect((self.low_pass_filter_1_0, 0), (self.blocks_add_xx_3, 1))
        self.connect((self.low_pass_filter_1_0, 0), (self.blocks_sub_xx_1, 1))
        self.connect((self.low_pass_filter_2, 0), (self.blocks_add_xx_3_0, 0))
        self.connect((self.low_pass_filter_2, 0), (self.qtgui_freq_sink_x_0_1_0_0_1_0, 0))
        self.connect((self.low_pass_filter_2, 0), (self.qtgui_waterfall_sink_x_0_1_0_0_1_0, 0))
        self.connect((self.low_pass_filter_2, 0), (self.rational_resampler_xxx_0_1_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_1_1, 0), (self.audio_sink_0_0_0_0_1, 0))
        self.connect((self.rds_encoder_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.satellites_bpsk_demodulator_0, 0), (self.blocks_float_to_char_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "FM_RDS")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 10500, 13500, 1500, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_3.set_taps(firdes.band_pass(1, self.samp_rate, 24000, 52000, 3000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_3_0.set_taps(firdes.band_pass(1, self.samp_rate, 11000, 14000, 3000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_3_1.set_taps(firdes.band_pass(1, self.samp_rate, 37500, 38500, 3000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_3_1_0.set_taps(firdes.band_pass(1, self.samp_rate, 55000, 59000, 3000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7500, 1500, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 14000, 3000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 14000, 1000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(1, self.samp_rate, 8000, 3000, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_1_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0_0_1_1.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=FM_RDS, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
