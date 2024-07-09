package de.upb.alarmClock;

import properties.PropertyManager;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class AlarmClock {
	
public static void main(String args[])
{
	//User Interface is Mandatory.
	//#if UserInterface
	final JFrame jframe = new JFrame("Alarm Clock");
	jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	jframe.setSize(1080,720);
	jframe.getContentPane().setLayout(null);
	jframe.setVisible(true);
	//#endif
	
	//#if TimerDisplay
	GuiStopwatch stp = new GuiStopwatch(jframe);
	//#endif
	
	//Miliseonds feature in GuiStopwatch
	
	//DarkLightMode feature in GuiStopwatch
	
	//Future features to be implemented
	PropertyManager.getProperty("ManualTimeChange");
	if (PropertyManager.getProperty("ManualTimeChange"))
	{
		System.out.println("ManualTimeChange");
	}
	
	PropertyManager.getProperty("SyncWithComputer");
	if (PropertyManager.getProperty("SyncWithComputer"))
	{
		System.out.println("SyncWithComputer");
	}
	
	PropertyManager.getProperty("AlternateColor");
	if (PropertyManager.getProperty("AlternateColor"))
	{
		System.out.println("AlternateColor");
	}
	
	PropertyManager.getProperty("DifferentTimezones");
	if (PropertyManager.getProperty("DifferentTimezones"))
	{
		System.out.println("DifferentTimezones");
	}
	
	PropertyManager.getProperty("Germany");
	if (PropertyManager.getProperty("Germany"))
	{
		System.out.println("Germany");
	}
	
	PropertyManager.getProperty("USA");
	if (PropertyManager.getProperty("USA"))
	{
		System.out.println("USA");
	}
	
	PropertyManager.getProperty("Korea");
	if (PropertyManager.getProperty("Korea"))
	{
		System.out.println("Korea");
	}
	
	PropertyManager.getProperty("Stopwatch");
	if (PropertyManager.getProperty("Stopwatch"))
	{
		System.out.println("Stopwatch");
	}
	
	PropertyManager.getProperty("ResetStopwatch");
	if (PropertyManager.getProperty("ResetStopwatch"))
	{
		JButton resetButton = new JButton("Reset");
		
		resetButton.setBounds(400,700,100,50);
		//resetButton.setFont(font);
		resetButton.setFocusable(false);
		//.addActionListener(this);
		
		jframe.getContentPane().add(resetButton);
		
		System.out.println("ResetStopwatch");
	}
	
	PropertyManager.getProperty("NewAlarm");
	if (PropertyManager.getProperty("NewAlarm"))
	{
		System.out.println("NewAlarm");
	}
	
	PropertyManager.getProperty("DeleteOldAlarm");
	if (PropertyManager.getProperty("DeleteOldAlarm"))
	{
		System.out.println("DeleteOldAlarm");
	}
	
	PropertyManager.getProperty("SaveInformation");
	if (PropertyManager.getProperty("SaveInformation"))
	{
		System.out.println("SaveInformation");
	}
	
	PropertyManager.getProperty("PDF");
	if (PropertyManager.getProperty("PDF"))
	{
		System.out.println("PDF");
	}
	
	PropertyManager.getProperty("Text");
	if (PropertyManager.getProperty("Text"))
	{
		System.out.println("Text");
	}
	
	PropertyManager.getProperty("Clear");
	if (PropertyManager.getProperty("Clear"))
	{
		System.out.println("Clear");
	}
	
	PropertyManager.getProperty("SaveSettings");
	if (PropertyManager.getProperty("SaveSettings"))
	{
		System.out.println("SaveSettings");
	}
	
}
}
