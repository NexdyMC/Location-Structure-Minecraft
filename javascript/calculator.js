// jQuery
$(document).ready(function(e) {
	function calculate (angleA, pointAx, pointAz, angleB, pointBx, pointBz) {
		var deg2rad = Math.PI/180;
		var rad2deg = 180/Math.PI;
		
		if (angleA >= 90) {
			angleA = Number((180-angleA))+Number(90);
		} else {
			angleA = -1*(Number(angleA)+Number(90));
		}
		
		if (angleB >= 90) {
			angleB = Number((180-angleB))+Number(90);
		} else {
			angleB = -1*(Number(angleB)+Number(90));
		}
		
		var slopeA = -1*Math.tan(angleA * deg2rad),
			slopeB = -1*Math.tan(angleB * deg2rad);
			
		// (-Z) = MX + B solve for B, then set equations equal to each other
		
		// Equation of Line for point A
		// -1*pointAz = slopeA*pointAx + B
		// -1*pointAz - slopeA*pointAx = B
		var interceptA = pointAz - slopeA*pointAx,
			interceptB = pointBz - slopeB*pointBx;
		
			
		// Solve for X
		// slopeA*X + interceptA = slopeB*X + interceptB
		// (slopeA-slopeB)*X = interceptB - interceptA
		// X = (interceptB - interceptA)/(slopeA-slopeB)
		var X = (interceptB - interceptA)/(slopeA-slopeB),
			Z = slopeA*X + interceptA;
		
		return Math.round(X)+','+Math.round(Z);
	}
	
	$('input[name=calculate]').click(function(e) {
		var angleA = $('input[name=angleA]').val(),
			pointAx = $('input[name=pointAx]').val(),
			pointAz = $('input[name=pointAz]').val(),
			angleB = $('input[name=angleB').val(),
			pointBx = $('input[name=pointBx]').val(),
			pointBz = $('input[name=pointBz]').val(),
			result = calculate(angleA, pointAx, pointAz, angleB, pointBx, pointBz),
			coords = result.split(',');
		$('#result').stop(true,true).hide().fadeIn(500).text('You see a Stronghold at X:'+coords[0]+', Z:'+coords[1]);
		
		
    });
});