using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tiner
{
    public partial class Form1 : Form
    {
        int seconds;
        int length;
        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime startTime = System.DateTime.Now;
            seconds = startTime.Hour * 3600 + startTime.Minute * 60 + startTime.Second;
            length = int.TryParse(textBox1.Text,out length)?int.Parse(textBox1.Text):3600;//Length of the timer in seconds.
            length = seconds + length;
            this.TopMost = false;
            timer1.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (length > seconds)
            {
                seconds++;
            }
            else
            {
                if (this.WindowState == FormWindowState.Minimized)
                {
                    this.WindowState = FormWindowState.Normal;
                }
                this.Activate();
                this.MaximizeBox = true;
                this.TopMost = true;
                //timer1.Stop();//Enable this if you don't want the timer to stay on top forever after time is over.
            }
            label1.Text = string.Format("Time Left: {0}:{1}:{2}", (length-seconds) / 3600, ((length-seconds) % 3600) / 60, ((length-seconds) % 3600) % 60);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
