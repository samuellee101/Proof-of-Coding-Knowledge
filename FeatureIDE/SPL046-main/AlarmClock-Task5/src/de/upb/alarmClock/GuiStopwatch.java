package de.upb.alarmClock;
import javax.swing.*;
import loader.PluginLoader;
import java.awt.*;
import java.awt.event.ActionListener;
import java.util.concurrent.TimeUnit;
import java.util.List;
import java.awt.event.ActionEvent;
import com.google.common.base.*;

import interfaces.Maininterface;
import loader.PluginLoader;

public class GuiStopwatch implements ActionListener {
	JButton startButton = new JButton("Start");
	JLabel timeLabel = new JLabel();
	JFrame contextFrame; 

	long currenttime = 0;
	long resetTime;
	long seconds = 0;
	long minutes = 0;
	long hours = 0;
	long miliseconds = 0;
	long addedHours = 0;
	
	String s;
	String min;
	String h;
	String mil;
	
	
	boolean started = false;
	
	Stopwatch stopwatch = Stopwatch.createUnstarted();
	
	Timer timer = new Timer( 1, new ActionListener() {
		@Override
		public void actionPerformed(ActionEvent e) {
			currenttime = stopwatch.elapsed(TimeUnit.MILLISECONDS) - resetTime;
			hours = (currenttime / 3600000) + addedHours;
			minutes = (currenttime / 60000) % 60;
			seconds = (currenttime / 1000) % 60;
			miliseconds = (currenttime) % 1000;
			mil = String.format("%03d", miliseconds);
			s = String.format("0%2d", seconds);
			min = String.format("0%2d", minutes);
			h = String.format("0%2d", hours);
			
	
			timeLabel.setText(h + " : " + min + " : " + s);
			//#if Miliseconds
			timeLabel.setText(h + " : " + min + " : " + s + " : " + mil);
			//#endif

		}
	}
	);
	
	
	
	
	GuiStopwatch(JFrame cFrame) {
		this.contextFrame = cFrame;
		timeLabel.setText(h + " : " + min + " : " + s);
		//#if Miliseconds
		timeLabel.setText(h + " : " + min + " : " + s + " : " + mil);
		//#endif
		timeLabel.setBounds(100,100,300,100);
		Font font = new Font("Times New Roman", Font.PLAIN, 35);
		timeLabel.setFont(font);
		timeLabel.setBorder(BorderFactory.createBevelBorder(1));
		timeLabel.setOpaque(true);
		timeLabel.setHorizontalAlignment(JTextField.CENTER);
		
		startButton.setBounds(50,550,250,70);
		startButton.setFont(font);
		startButton.setFocusable(false);
		startButton.addActionListener(this);
		
		//potentially change into its own feature
		contextFrame.getContentPane().add(startButton);
		
		contextFrame.getContentPane().add(timeLabel);
		
		//#if DarkLightMode
		JButton darkLight = new JButton("Light / Dark");
		darkLight.setEnabled(true);
 		
		darkLight.addActionListener(new ActionListener() {
 		
			public void actionPerformed(ActionEvent e) {
 				
 				//tracker needs to be updated upon each actionPerformed
				Color tracker = contextFrame.getContentPane().getBackground();
 				
 				if (tracker != Color.WHITE)
 				{
 					contextFrame.getContentPane().setBackground(Color.WHITE);
 				}
 				else if (tracker == Color.WHITE)
 				{
 					contextFrame.getContentPane().setBackground(Color.BLACK);
 				}
 			}
 		});
 		
 		darkLight.setBounds(50, 430, 250, 70);
 		contextFrame.getContentPane().add(darkLight);
		//#endif
		
		//#if AddHour
 				JButton addHour = new JButton("Add Hour");
 				addHour.setEnabled(true);
 				
 				addHour.addActionListener(new ActionListener() {
 				
 					public void actionPerformed(ActionEvent e) {
 						
 						addedHours = addedHours + 1;
 					}
 				});
 		
 		addHour.setBounds(400, 430, 250, 70);
 		contextFrame.getContentPane().add(addHour);
		//#endif
		
		//#if Clear
 				JButton ClearButton = new JButton("ClearButton");
 				ClearButton.setEnabled(true);
 				
 				ClearButton.addActionListener(new ActionListener() {
 				
 					public void actionPerformed(ActionEvent e) {
 						addedHours = 0;
 						timer.restart();
 						resetTime = stopwatch.elapsed(TimeUnit.MILLISECONDS);
 						mil = "";
 						s = "";
 						min = "";
 						h = "";
 						timeLabel.setText(h + " : " + min + " : " + s);
						//#if Miliseconds
 						timeLabel.setText(h + " : " + min + " : " + s + " : " + mil);
						//#endif
 					}
 				});
 				
 				ClearButton.setBounds(50, 310, 250, 70);
 				contextFrame.getContentPane().add(ClearButton);
		//#endif
		
		
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == startButton) {
			if (started == false) {
				started = true;
				System.out.println("Should be started;");
				startButton.setText("Stop");
				start();
			}
			else {
				started = false;
				startButton.setText("START");
				stop();
			}
		}
	}
	
	void start() {
		this.timer.start();
		this.stopwatch.start();
	}
	
	void stop() {
		this.timer.stop();
		this.stopwatch.stop();
	}
	
	// PlugIn Loader 
	List<Maininterface> buttonPlugins = PluginLoader.load(Maininterface.class);
	{
	for (Maininterface button : buttonPlugins) {
		//button.addButton(AddHour, Clear, DarkLightMode, Miliseconds, TimerDisplay, UserInterface);
		button.addButton(contextFrame, addedHours);
	}
	}
	
	
}

