/**
 * Vercel Speed Insights Integration
 * This script initializes Vercel Speed Insights for the static HTML site.
 * 
 * Note: Speed Insights must be enabled in the Vercel dashboard for this project.
 * After enabling, Vercel will automatically inject the tracking script.
 * 
 * This file provides the initialization queue for the Speed Insights SDK.
 */

// Initialize Speed Insights queue
(function() {
  'use strict';
  
  // Create the Speed Insights queue if it doesn't exist
  if (window.si) return;
  
  window.si = function() {
    (window.siq = window.siq || []).push(arguments);
  };
  
  // The actual Speed Insights script will be loaded by Vercel
  // after you enable Speed Insights in your project dashboard
  console.log('[Speed Insights] Queue initialized. Enable Speed Insights in Vercel dashboard to activate tracking.');
})();
